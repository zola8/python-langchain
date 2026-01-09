from typing import TypedDict, Annotated

from langchain_core.messages import HumanMessage
from langchain_ollama import ChatOllama
from langgraph.constants import END
from langgraph.graph import StateGraph, add_messages

llm = ChatOllama(model="llama3.2", temperature=0.2)  # llama3.2 - qwen3:4b


class State(TypedDict):
    messages: Annotated[list, add_messages]


GENERATE_POST = "generate_post"
GET_REVIEW_DECISION = "get_review_decision"
POST = "post"
COLLECT_FEEDBACK = "collect_feedback"


def generate_post(state: State):
    return {
        "messages": [llm.invoke(state["messages"])]
    }


def get_review_decision(state: State):
    post_content = state["messages"][-1].content

    print("\n📢 Current Social media Post:\n")
    print(post_content)
    print("\n")

    decision = input("Post to Social media? (yes/no): ")

    if decision.lower() == "yes":
        return POST
    else:
        return COLLECT_FEEDBACK


def post(state: State):
    final_post = state["messages"][-1].content
    print("\n📢 Final Social media Post:\n")
    print(final_post)
    print("\n✅ Post has been approved and is now live on Social media!")


def collect_feedback(state: State):
    feedback = input("How can I improve this post?")
    return {
        "messages": [HumanMessage(content=feedback)]
    }


graph = StateGraph(State)

graph.add_node(GENERATE_POST, generate_post)
graph.add_node(GET_REVIEW_DECISION, get_review_decision)
graph.add_node(COLLECT_FEEDBACK, collect_feedback)
graph.add_node(POST, post)

graph.set_entry_point(GENERATE_POST)

graph.add_conditional_edges(GENERATE_POST, get_review_decision)
graph.add_edge(POST, END)
graph.add_edge(COLLECT_FEEDBACK, GENERATE_POST)

app = graph.compile()

# core agent loop:
#   query -> ( model -> tools ) -> answer

# human in the agent loop:
#   query -> ( model -> tools ) <--> human-in-model -> answer

# https://github.com/harishneel1/langgraph/blob/main/8_human-in-the-loop/1_using_input().py
if __name__ == "__main__":
    response = app.invoke({
        "messages": [HumanMessage(content="Write me a Social media post on AI Agents taking over content creation")]
    })

    print(response)

    # for msg in response['messages']:
    #     print(msg.content)
