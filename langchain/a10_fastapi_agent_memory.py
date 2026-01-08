import uvicorn
from fastapi import FastAPI
from langchain.agents import create_agent
from langchain_core.messages import HumanMessage
from langchain_core.runnables import RunnableConfig
from langchain_ollama import ChatOllama
from langgraph.checkpoint.memory import InMemorySaver

app = FastAPI()

llm = ChatOllama(model="llama3.2", temperature=0.2)  # llama3.2 - qwen3:4b

agent = create_agent(
    model=llm,
    system_prompt="Assist users in finding information. Be brief and short.",
    tools=[],
    checkpointer=InMemorySaver(),  # comment out = without memory
)


@app.post("/", tags=["ask"])
def ask(question: str) -> str:
    # Input must be a dict with "messages" key
    input_messages = {"messages": [HumanMessage(content=question)]}
    config: RunnableConfig = {"configurable": {"thread_id": "123"}}

    response = agent.invoke(input_messages, config)

    # Last message is the answer
    last_message_content = response["messages"][-1].content
    print(question)
    print(last_message_content)
    return last_message_content


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8080)
