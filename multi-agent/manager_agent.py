# manager_agent.py
from langchain_core.messages import SystemMessage
from langgraph.graph import MessagesState, END
from langgraph.types import Command

from base_agent import BaseSubAgent


class ManagerAgent:
    def __init__(self, model, sub_agents: list[BaseSubAgent]):
        self.model = model
        self.sub_agents = {agent.name: agent for agent in sub_agents}
        self.agent_names = list(self.sub_agents.keys())

    def __call__(self, state: MessagesState):
        prompt = f"""You are a supervisor managing a team of workers.
Workers: {', '.join(self.agent_names)}

Your task is to route the user's request to the correct worker based on their description.
If the worker has completed the task and you have the final answer, route to 'FINISH'.
Otherwise, route to the exact name of the worker needed.

Respond with ONLY the exact name of the worker or 'FINISH'. Do not add punctuation.
"""
        messages = [SystemMessage(content=prompt)] + state["messages"]
        response = self.model.invoke(messages)

        # Simple routing logic based on the LLM's text output
        content = response.content.strip().upper()
        next_node = "FINISH"
        for name in self.agent_names:
            if name.upper() in content:
                next_node = name
                break

        # Use LangGraph's Command to route without polluting the message history
        if next_node == "FINISH":
            return Command(goto=END)

        return Command(goto=next_node)
