from langchain.tools import tool
from langchain_ollama import ChatOllama

llm = ChatOllama(model="qwen3:4b", temperature=0.2)


@tool
def say_hi(name: str) -> str:
    "Use this tool to greet people"
    return f"Hi {name}"


@tool
def say_bye(name: str) -> str:
    "Use this tool to bid farewell to people"
    return f"Bye {name}"


tools = [say_hi, say_bye]
llm_with_tools = llm.bind_tools(tools)

# Tool Execution Loops
# https://github.com/krishnaik06/Langchain-V1-Crash-Course/blob/main/updatedlangchain/3-tools.ipynb

if __name__ == "__main__":
    # Step 1: Model generates tool calls
    query = "My sister named Gisel is coming to my house, what should I say?"
    messages = [{"role": "user", "content": query}]
    ai_msg = llm_with_tools.invoke(messages)
    messages.append(ai_msg)

    # Step 2: Execute tools and collect results
    for tool_call in ai_msg.tool_calls:
        # Execute the tool with the generated arguments
        tool_result = say_hi.invoke(tool_call)
        messages.append(tool_result)

    # Step 3: Pass results back to model for final response
    final_response = llm_with_tools.invoke(messages)
    print(final_response.text)
