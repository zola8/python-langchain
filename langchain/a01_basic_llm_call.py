from langchain_core.messages import SystemMessage, HumanMessage
from langchain_ollama import ChatOllama

llm = ChatOllama(
    model="llama3.2",
    temperature=0.2,
)

if __name__ == "__main__":
    system_msg = SystemMessage("You are a helpful assistant.")
    human_msg = HumanMessage("Hello, how are you?")

    # Use with chat models
    messages = [system_msg, human_msg]

    # Get response
    response = llm.invoke(messages)

    # Print the response content
    print(response.content)
