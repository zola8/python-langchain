from fastmcp import FastMCP, Context

mcp = FastMCP("My MCP Server 🚀")


@mcp.tool(description="Greeting a user.")
def greet(name: str) -> str:
    return f"Hello, {name}!"


@mcp.tool(
    name="find_products",  # Custom tool name for the LLM
    description="Search the product catalog with optional category filtering.",  # Custom description
    tags={"catalog", "search"},  # Optional tags for organization/filtering
    meta={"version": "1.2", "author": "product-team"},  # Custom metadata
    annotations={
        "readOnlyHint": True,
        "openWorldHint": False,
        "idempotentHint": True,
    }
)
def search_products_implementation(query: str, category: str | None = None) -> list[dict]:
    """Internal function description (ignored if description is provided above)."""
    # Implementation...
    print(f"Searching for '{query}' in category '{category}'")
    return [{"id": 2, "name": f"Another Product of {query}"}]


@mcp.tool
def dynamic_tool():
    return "I am a dynamic tool."


@mcp.tool(enabled=False)
def maintenance_tool():
    """This tool is currently under maintenance."""
    return "This tool is disabled."


# Resource returning JSON data (dict is auto-serialized)
@mcp.resource("data://config")
def get_config() -> dict:
    """Provides application configuration as JSON."""
    return {
        "theme": "dark",
        "version": "1.2.0",
        "features": ["tools", "resources"],
    }


# Basic dynamic resource returning a string
@mcp.resource("resource://greeting")
def get_greeting() -> str:
    """Provides a simple greeting message."""
    return "Hello from FastMCP Resources!"


# Example specifying metadata
@mcp.resource(
    uri="data://app-status",  # Explicit URI (required)
    name="ApplicationStatus",  # Custom name
    description="Provides the current status of the application.",  # Custom description
    mime_type="application/json",  # Explicit MIME type
    tags={"monitoring", "status"},  # Categorization tags
    meta={"version": "2.1", "team": "infrastructure"}  # Custom metadata
)
def get_application_status() -> dict:
    """Internal function description (ignored if description is provided above)."""
    return {"status": "ok", "uptime": 12345, "settings": mcp.settings}  # Example usage


@mcp.resource("data://secret", enabled=False)
def get_secret_data():
    """This resource is currently disabled."""
    return "Secret data"


# Use async def for resource functions that perform I/O operations (e.g., reading from a database or network) to avoid blocking the server.
@mcp.resource("resource://{name}/details")
async def get_details(name: str, ctx: Context) -> dict:
    """Get details for a specific name."""
    return {
        "name": name,
        "accessed_at": ctx.request_id
    }


# Template URI includes {city} placeholder
@mcp.resource("weather://{city}/current")
def get_weather(city: str) -> dict:
    """Provides weather information for a specific city."""
    # In a real implementation, this would call a weather API
    # Here we're using simplified logic for example purposes
    return {
        "city": city.capitalize(),
        "temperature": 22,
        "condition": "Sunny",
        "unit": "celsius"
    }


# Basic prompt returning a string (converted to user message automatically)
@mcp.prompt
def ask_about_topic(topic: str) -> str:
    """Generates a user message asking for an explanation of a topic."""
    return f"Can you please explain the concept of '{topic}'?"


# https://gofastmcp.com/getting-started/quickstart

if __name__ == "__main__":
    dynamic_tool.disable()
    mcp.run(transport="http")

    # Use standard input/output (stdin and stdout) to receive and respond to tool function calls.
    # mcp.run(transport="stdio")
