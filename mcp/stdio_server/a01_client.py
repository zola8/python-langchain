# client.py
import asyncio

from fastmcp import Client

client = Client(transport="a01_server.py")


async def main():
    async with client:
        result = await client.call_tool(name="greet_user_tool", arguments={"name": "Zoltan"})
        print(result.content[-1].text)

# https://medium.com/@laurentkubaski/understanding-mcp-stdio-transport-protocol-ae3d5daf64db

if __name__ == "__main__":
    asyncio.run(main())
