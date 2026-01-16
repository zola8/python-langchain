import asyncio

from fastmcp import Client

client = Client("http://localhost:8000/mcp")


async def test_calls():
    async with client:
        result = await client.call_tool("weather_get_forecast", {"city": "London"})
        print("result:", result.content[-1].text)
        await client.call_tool("notes_add_note", {"content": "test 123"})
        result = await client.call_tool("notes_get_my_notes")
        print("result:", result.content[-1].text)


if __name__ == "__main__":
    asyncio.run(test_calls())
