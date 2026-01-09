from langchain.agents import create_agent
from langchain_ollama import ChatOllama

llm = ChatOllama(model="llama3.2", temperature=0.2)  # llama3.2 - qwen3:4b


def create_my_agent(my_llm=llm, my_tools=[], my_middleware=[]):
    return create_agent(
        model=my_llm,
        system_prompt="You are a helpful assistant.",
        tools=my_tools,
        middleware=my_middleware,
    )


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


if __name__ == "__main__":
    main_loop(create_my_agent())
