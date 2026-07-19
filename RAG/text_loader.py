from langchain_community.document_loaders import TextLoader
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_huggingface import HuggingFacePipeline
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
from dotenv import load_dotenv

load_dotenv()

# Load poem
loader = TextLoader("poem.txt", encoding="utf-8")
docs = loader.load()
print(docs[0])

# Load LFM2.5 model
model_id = "LiquidAI/LFM2.5-8B-A1B"

tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(
    model_id,
    device_map="auto",
    torch_dtype="bfloat16",
)

# Wrap in a text-generation pipeline
pipe = pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer,
    max_new_tokens=200,
    do_sample=True,
    temperature=0.3,
)

# Wrap for LangChain
llm = HuggingFacePipeline(pipeline=pipe)

# Prompt + chain
prompt = PromptTemplate(
    template="Write the summary of the following poem:\n\n{poem}",
    input_variables=["poem"]
)

parser = StrOutputParser()

chain = prompt | llm | parser

result = chain.invoke({"poem": docs[0].page_content})
print(result)