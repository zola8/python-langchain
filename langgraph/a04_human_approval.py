from typing import TypedDict, Annotated, List

from langchain_community.tools import DuckDuckGoSearchRun
from langchain_core.messages import HumanMessage
from langchain_ollama import ChatOllama
from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph import StateGraph, END, add_messages
from langgraph.prebuilt import ToolNode

memory = MemorySaver()
search_tool = DuckDuckGoSearchRun()
tools = [search_tool]
llm = ChatOllama(model="llama3.2", temperature=0.2)  # llama3.2 - qwen3:4b
llm_with_tools = llm.bind_tools(tools=tools)


class BasicState(TypedDict):
    messages: Annotated[List, add_messages]


def model(state: BasicState):
    return {
        "messages": [llm_with_tools.invoke(state["messages"])]
    }


def tools_router(state: BasicState):
    last_message = state["messages"][-1]
    if (hasattr(last_message, "tool_calls") and
            len(last_message.tool_calls) > 0):
        return "tools"
    else:
        return END


graph = StateGraph(BasicState)
graph.add_node(model, "model")
graph.add_node("tools", ToolNode(tools=tools))

graph.set_entry_point("model")
graph.add_conditional_edges("model", tools_router)

graph.add_edge("tools", "model")

app = graph.compile(checkpointer=memory, interrupt_before=["tools"])

if __name__ == "__main__":
    config = {"configurable": {
        "thread_id": 1
    }}

    events = app.stream({
        "messages": [HumanMessage(content="What is the current weather in Ho Chi Minh City?")]
    }, config=config, stream_mode="values")

    for event in events:
        event["messages"][-1].pretty_print()

    snapshot = app.get_state(config=config)
    print(snapshot.next)

    events = app.stream(None, config, stream_mode="values")
    for event in events:
        event["messages"][-1].pretty_print()

# app.invoke returns a value after the graph has exited (interrupted or end node reached)
# stream is a generator function that emits events after every single node
