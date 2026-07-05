# tools.py
from langchain_core.tools import tool


@tool
def get_weather(city: str) -> str:
    """Get the current weather for a specific city."""
    return f"The weather in {city} is sunny and 25°C."


@tool
def calculate_math(expression: str) -> str:
    """Evaluate a math expression (e.g., '2 + 2 * 5')."""
    try:
        # Note: eval is used here for demo simplicity. Use a safe parser in production.
        return str(eval(expression))
    except Exception as e:
        return f"Error calculating: {e}"


@tool
def search_web(query: str) -> str:
    """Search the web for information on a given topic."""
    return f"Top search results for '{query}': [Article 1, Article 2, Wikipedia link]"
