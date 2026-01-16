# https://gofastmcp.com/servers/composition#why-compose-servers

from fastmcp import FastMCP

# Define subservers
weather_mcp = FastMCP(name="WeatherService")


@weather_mcp.tool
def get_forecast(city: str) -> dict:
    """Get weather forecast."""
    return {"city": city, "forecast": "Sunny"}


@weather_mcp.resource("data://cities/supported")
def list_supported_cities() -> list[str]:
    """List cities with weather support."""
    return ["London", "Paris", "Tokyo"]


if __name__ == "__main__":
    pass
