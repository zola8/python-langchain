from base_agent import BaseSubAgent
from tools import search_web


class SearchAgent(BaseSubAgent):
    def __init__(self, model):
        super().__init__(
            name="search_agent",
            description="Handles general knowledge queries and web searches.",
            model=model,
            tools=[search_web]
        )
