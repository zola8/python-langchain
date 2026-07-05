# base_agent.py
from langchain.agents import create_agent
from langchain_core.language_models import BaseChatModel
from langchain_core.tools import BaseTool
from langgraph.graph import MessagesState


class BaseSubAgent:
    def __init__(self, name: str, description: str, model: BaseChatModel, tools: list[BaseTool]):
        self.name = name
        self.description = description
        self.agent = create_agent(
            model,
            tools=tools,
            system_prompt="You are a helpful assistant. Be concise and accurate.",
        )

    def __call__(self, state: MessagesState):
        config = {"configurable": {"thread_id": str("aaa123")}}

        return self.agent.invoke(state)
