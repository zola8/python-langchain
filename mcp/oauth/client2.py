import asyncio
import os

from dotenv import load_dotenv
from fastmcp import Client

load_dotenv()

BASE_URL = os.getenv("BASE_URL") + "/mcp"


async def main():
    async with Client(BASE_URL, auth="oauth") as client:
        # Ensure client can connect
        await client.ping()

        # List available operations
        tools = await client.list_tools()
        print(tools)
        resources = await client.list_resources()
        prompts = await client.list_prompts()

        # Ex. execute a tool call
        # result = await client.call_tool("your_example_tool", {"param": "value"})
        # print(result)

        # Test the protected tool
        result = await client.call_tool("get_user_info")
        print(result)


asyncio.run(main())
