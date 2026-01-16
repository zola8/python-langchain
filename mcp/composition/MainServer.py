import asyncio

from fastmcp import FastMCP

from NoteServer import notes_mcp
from WeatherServer import weather_mcp

# Define main server
main_mcp = FastMCP(name="MainApp")


# Import subserver = composition
async def setup():
    await main_mcp.import_server(weather_mcp, prefix="weather")
    await main_mcp.import_server(notes_mcp, prefix="notes")


# Result: main_mcp now contains prefixed components:
# - Tool: "weather_get_forecast"
# - Resource: "data://weather/cities/supported"

if __name__ == "__main__":
    asyncio.run(setup())
    main_mcp.run(transport="http")
