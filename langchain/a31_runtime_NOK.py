from dataclasses import dataclass

from langchain.agents import create_agent
from langchain_ollama import ChatOllama

llm = ChatOllama(model="llama3.2", temperature=0.2)  # llama3.2 - qwen3:4b


@dataclass
class Context:
    user_name: str


agent = create_agent(
    model=llm,
    tools=[],
    context_schema=Context
)

if __name__ == "__main__":
    result = agent.invoke(
        {"messages": [{"role": "user", "content": "What's my user name?"}]},
        context=Context(user_name="John Smith")
    )

    print(result['messages'][-1].content)
