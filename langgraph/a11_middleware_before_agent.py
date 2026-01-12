from typing import Any

from langchain.agents import create_agent
from langchain.agents.middleware import before_agent, AgentState
from langchain_ollama import ChatOllama
from langgraph.runtime import Runtime

banned_keywords = ["hack", "exploit", "malware"]


@before_agent(can_jump_to=["end"])
def content_filter(state: AgentState, runtime: Runtime) -> dict[str, Any] | None:
    """Deterministic guardrail: Block requests containing banned keywords."""
    # Get the first user message
    if not state["messages"]:
        return None

    last_message = state["messages"][-1]
    if last_message.type != "human":
        return None

    content = last_message.content.lower()

    # Check for banned keywords
    for keyword in banned_keywords:
        if keyword in content:
            # Block execution before any processing
            return {
                "messages": [{
                    "role": "assistant",
                    "content": "BANNED content! Please rephrase your request."
                }],
                "jump_to": "end"
            }

    return None


llm = ChatOllama(model="llama3.2", temperature=0.2)  # llama3.2 - qwen3:4b


def main_loop(agent):
    history = []
    while True:
        user_input = input("You: ")
        if user_input.lower() in {"exit", "quit"}:
            break

        history.append({"role": "user", "content": user_input})

        result = agent.invoke({"messages": history})
        assistant_msg = result["messages"][-1].content
        print("Assistant:", assistant_msg, "\n")

        history.append({"role": "assistant", "content": assistant_msg})


# https://docs.langchain.com/oss/python/langchain/guardrails#before-agent-guardrails

if __name__ == "__main__":
    agent = create_agent(
        model=llm,
        middleware=[content_filter],
    )

    main_loop(agent)

    # result = agent.invoke({
    #     "messages": [{"role": "user", "content": "How do I hack into a database?"}]
    # })
    # print(result)
