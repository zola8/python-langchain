from langchain.agents import create_agent
from langchain_core.messages import HumanMessage
from langchain_ollama import ChatOllama

llm = ChatOllama(model="llama3.2", temperature=0.2)  # llama3.2 - qwen3:4b

agent = create_agent(
    model=llm,
    system_prompt="Assist users in finding information. Be brief and short.",
)

if __name__ == "__main__":
    messages = {"messages": [HumanMessage("What is python programming language?")]}
    response = agent.invoke(input=messages)
    print(f"{response['messages'][1].content}")
