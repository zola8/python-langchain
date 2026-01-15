import asyncio

from fastmcp import Client

client = Client("http://localhost:8000/mcp")


async def list_tools():
    async with client:
        result = await client.list_tools()
        for tool_item in result:
            print(f"name: {tool_item.name}, description: {tool_item.description}")
            # print(tool_item)


async def call_tool(name: str):
    async with client:
        result = await client.list_tools()
        print(result)

        result = await client.call_tool("greet", {"name": name})
        print(result)


if __name__ == "__main__":
    asyncio.run(list_tools())
    # asyncio.run(call_tool("Zola"))
