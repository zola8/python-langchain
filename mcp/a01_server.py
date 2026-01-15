from fastmcp import FastMCP

mcp = FastMCP("My MCP Server 🚀")


@mcp.tool(description="Greeting a user.")
def greet(name: str) -> str:
    return f"Hello, {name}!"


# https://gofastmcp.com/getting-started/quickstart

if __name__ == "__main__":
    mcp.run(transport="http")

    # Use standard input/output (stdin and stdout) to receive and respond to tool function calls.
    # mcp.run(transport="stdio")
