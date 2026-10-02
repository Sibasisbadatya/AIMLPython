# %%
from contextlib import asynccontextmanager
from typing import TypedDict, Annotated

from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
from langchain_core.messages import BaseMessage, HumanMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.checkpoint.sqlite.aio import AsyncSqliteSaver
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from pydantic import BaseModel, Field
from langgraph.prebuilt import ToolNode, tools_condition
from langchain_core.tools import tool
from langchain_community.tools import DuckDuckGoSearchRun
import requests  # 👈 Add this import

# %%
import os
load_dotenv()
# %%

# ---------- State & request models ----------
class ChatState(TypedDict):
    messages: Annotated[list[BaseMessage], add_messages]


class ChatRequest(BaseModel):
    message: str = Field(..., description="The message from the user")
    thread_id: str = Field(..., description="thread id for the chat conversation")
    
    
    

# %%
# ---------- Model & graph ----------
model = ChatGoogleGenerativeAI(model="gemini-3.1-flash-lite", streaming=True)

# %%
async def chat_node(state: ChatState):
    response = await llm_with_tools.ainvoke(state["messages"]) # 👈 Uses the model with tools
    return {"messages": [response]}

# %%

search_tool = DuckDuckGoSearchRun(region="us-en")

@tool
def calculator(first_num: float, second_num: float, operation: str) -> dict:
    """
    Perform a basic arithmetic operation on two numbers.
    Supported operations: add, sub, mul, div
    """
    try:
        if operation == "add":
            result = first_num + second_num
        elif operation == "sub":
            result = first_num - second_num
        elif operation == "mul":
            result = first_num * second_num
        elif operation == "div":
            if second_num == 0:
                return {"error": "Division by zero is not allowed"}
            result = first_num / second_num
        else:
            return {"error": f"Unsupported operation '{operation}'"}
        
        return {"first_num": first_num, "second_num": second_num, "operation": operation, "result": result}
    except Exception as e:
        return {"error": str(e)}




@tool
def get_stock_price(symbol: str) -> dict:
    """
    Fetch latest stock price for a given symbol (e.g. 'AAPL', 'TSLA') 
    using Alpha Vantage with API key in the URL.
    """
    url = f"https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey=4577EQBWMB2BD1HI"
    r = requests.get(url)
    return r.json()


# %%

tools = [get_stock_price,calculator,search_tool]
llm_with_tools = model.bind_tools(tools=tools)

tool_node = ToolNode(tools=tools)


# %%

graph = StateGraph(ChatState)
graph.add_node("chat_node", chat_node)
graph.add_node("tools",tool_node)

graph.add_edge(START, "chat_node")
graph.add_conditional_edges("chat_node", tools_condition)
graph.add_edge("tools", "chat_node")
# graph.add_edge("chat_node", END)

# %%

# ---------- App with async checkpointer ----------
@asynccontextmanager
async def lifespan(app: FastAPI):
    async with AsyncSqliteSaver.from_conn_string("chetbot.db") as checkpointer:
        app.state.checkpointer = checkpointer
        chabot = graph.compile(checkpointer=checkpointer)
        app.state.chatbot = chabot
        # Example
        drawable_graph = chabot.get_graph()
        print(drawable_graph.draw_ascii())
        yield


# %%
app = FastAPI(lifespan=lifespan)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# %%
@app.post("/chat")
async def chat(req: ChatRequest):
    chatbot = app.state.chatbot

    async def generate():
        config = {"configurable": {"thread_id": req.thread_id}}
        async for event in chatbot.astream_events(
            {"messages": [HumanMessage(content=req.message)]},
            config=config,
            version="v2",
        ):
            # print("Event",event)
            if event["event"] == "on_chat_model_stream":
                chunk = event["data"]["chunk"]
                if isinstance(chunk.content, list):
                    for part in chunk.content:
                        if part.get("type") == "text":
                            yield part["text"]
                elif isinstance(chunk.content, str):
                    yield chunk.content

    return StreamingResponse(generate(), media_type="text/plain")

# %%
@app.get("/conversation/{thread_id}")
async def get_conversation(thread_id: str):
    config = {"configurable": {"thread_id": thread_id}}
    try:
        state = await app.state.chatbot.aget_state(config)  # async version
        messages = state.values.get("messages", [])
        return {
            "thread_id": thread_id,
            "messages": [{"type": m.type, "content": m.content} for m in messages],
        }
    except Exception as e:
        return {"error": str(e)}


# %%
@app.get("/threads")
async def get_threads():

    threads = set()

    async for checkpoint in app.state.checkpointer.alist(None):
        config = checkpoint.config

        thread_id = (
            config.get("configurable", {})
                  .get("thread_id")
        )

        if thread_id:
            threads.add(thread_id)

    return {"threads": list(threads)}
# %%
