import asyncio

from fastmcp import Client

client = Client("http://localhost:8000/mcp")


async def list_tools():
    async with client:
        result = await client.list_tools()
        for tool_item in result:
            # print(f"name: {tool_item.name}, description: {tool_item.description}")
            print(tool_item)


async def call_tools():
    async with client:
        result = await client.list_tools()
        print(result)

        result = await client.call_tool("greet", {"name": "Zola"})
        print(result)

        result = await client.call_tool("find_products", {"query": "biscuit", "category": "food"})
        print(result)


async def call_resources():
    async with client:
        result = await client.list_resources()
        print("Available resources:")
        for res in result:
            print("\t", res)

        print("\n-- greeting:")
        result = await client.read_resource("resource://greeting")
        print("result:", result[-1].text)

        print("\n-- get_config:")
        result = await client.read_resource("data://config")
        print("result:", result[-1].text)

        print("\n-- app-status:")
        result = await client.read_resource("data://app-status")
        print("result:", result[-1].text)

        print("\n-- weather:")
        result = await client.read_resource("weather://London/current")
        print("result:", result[-1].text)


async def call_prompts():
    async with client:
        result = await client.get_prompt("ask_about_topic", {"topic": "flower"})
        print("result:", result.messages[-1].content.text)


if __name__ == "__main__":
    # asyncio.run(list_tools())
    # asyncio.run(call_tools())
    # asyncio.run(call_resources())
    asyncio.run(call_prompts())
