# The Graph Orchestrator (graph.py)
# This class builds the LangGraph StateGraph, connects the nodes, and compiles it.

# graph.py
from langgraph.graph import StateGraph, MessagesState, START

from base_agent import BaseSubAgent
from manager_agent import ManagerAgent


class AgentGraph:
    def __init__(self, manager: ManagerAgent, sub_agents: list[BaseSubAgent]):
        self.manager = manager
        self.sub_agents = {agent.name: agent for agent in sub_agents}
        self.graph = self._build_graph()

    def _build_graph(self):
        workflow = StateGraph(MessagesState)

        # Add Manager Node
        workflow.add_node("manager", self.manager)

        # Add Sub-Agent Nodes
        for name, agent in self.sub_agents.items():
            workflow.add_node(name, agent)

        # Define Edges
        workflow.add_edge(START, "manager")

        # Sub-agents always route back to the manager after they finish their internal tool loop
        for name in self.sub_agents.keys():
            workflow.add_edge(name, "manager")

        return workflow.compile()

    def invoke(self, inputs: dict):
        return self.graph.invoke(inputs)
