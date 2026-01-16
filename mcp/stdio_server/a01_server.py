# server.py
from fastmcp import FastMCP

server = FastMCP("Greetings")


@server.tool()
async def greet_user_tool(name: str) -> str:
    result = f"Good day to you, {name}. I trust this message finds you well."
    return result


if __name__ == "__main__":
    server.run(transport="stdio")
