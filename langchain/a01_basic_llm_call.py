from langchain_core.messages import SystemMessage, HumanMessage
from langchain_ollama import ChatOllama

llm = ChatOllama(
    model="qwen3:latest",
    temperature=0.2,
)

if __name__ == "__main__":
    system_msg = SystemMessage("You are a helpful assistant.")
    human_msg = HumanMessage("Why is the sky blue?")

    # Use with chat models
    messages = [system_msg, human_msg]

    # Get response
    response = llm.invoke(messages)

    # Print the response content
    print(response.content)
