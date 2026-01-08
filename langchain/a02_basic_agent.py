from langchain.agents import create_agent
from langchain_ollama import ChatOllama

llm = ChatOllama(
    model="llama3.2",
    temperature=0.2,
)

agent = create_agent(
    model=llm,
    system_prompt="You are a helpful assistant",
)

if __name__ == "__main__":
    res = agent.invoke(
        {"messages": [{"role": "user", "content": "what is water?"}]}
    )

    print(res['messages'][1].content)
