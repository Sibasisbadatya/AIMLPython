def main() -> None:
    print("Hello from mcp-server!")
import random

from fastmcp import FastMCP

# create a FastMCP instance
mcp = FastMCP(name="Demo Server")

@mcp.tool
def rollDice(n_dice:int)->list[int]:
    """Rolls n_dice and returns the results as a list of integers."""
    return [random.randint(1, 6) for _ in range(n_dice)]


if __name__ == "__main__":
    main()
