from typing import TypedDict

from langchain_core.runnables import RunnableConfig
from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph import StateGraph, END
from langgraph.types import Command, interrupt

memory = MemorySaver()


class State(TypedDict):
    value: str


def node_a(state: State):
    print("Node A")
    return Command(
        goto="node_b",
        update={
            "value": state["value"] + "a"
        }
    )


def node_b(state: State):
    print("Node B")

    human_response = interrupt("Do you want to go to C or D? Type C/D")

    print("Human Review Values: ", human_response)

    if (human_response == "C"):
        return Command(
            goto="node_c",
            update={
                "value": state["value"] + "b"
            }
        )
    elif (human_response == "D"):
        return Command(
            goto="node_d",
            update={
                "value": state["value"] + "b"
            }
        )
    return None


def node_c(state: State):
    print("Node C")
    return Command(
        goto=END,
        update={
            "value": state["value"] + "c"
        }
    )


def node_d(state: State):
    print("Node D")
    return Command(
        goto=END,
        update={
            "value": state["value"] + "d"
        }
    )


graph = StateGraph(State)

graph.add_node("node_a", node_a)
graph.add_node("node_b", node_b)
graph.add_node("node_c", node_c)
graph.add_node("node_d", node_d)

graph.set_entry_point("node_a")

app = graph.compile(checkpointer=memory)

# https://github.com/harishneel1/langgraph/blob/main/8_human-in-the-loop/3_resume.ipynb
# https://www.youtube.com/watch?v=3MsGtLN793w
if __name__ == "__main__":
    config: RunnableConfig = {"configurable": {"thread_id": "1"}}

    initialState = {
        "value": ""
    }

    first_result = app.invoke(initialState, config, stream_mode="updates")
    print(first_result)
    print(app.get_state(config).next)

    second_result = app.invoke(Command(resume="C"), config=config, stream_mode="updates")
    print(second_result)
