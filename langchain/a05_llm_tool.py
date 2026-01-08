from langchain.tools import tool
from langchain_core.messages import HumanMessage, ToolMessage
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

if __name__ == "__main__":
    query = "My sister named Gisel is coming to my house, what should I say?"
    messages = [HumanMessage(query)]
    output = llm_with_tools.invoke(messages)
    messages.append(output)

    print(messages)
    tool_calls = output.tool_calls
    print(tool_calls)
    print('selected tool:', tool_calls[0]['name'])
    print('argument that will be passed to the tool:', tool_calls[0]['args'])

    tool_mapping = {'say_hi': say_hi, 'say_bye': say_bye}  # mapping between tool name and defined tool function
    selected_tool = tool_mapping[tool_calls[0]['name']]  # used to get the selected tool
    tool_output = selected_tool.invoke(tool_calls[0]['args'])  # invoke the selected tool with the argument
    print("tool_output:", tool_output)

    messages.append(ToolMessage(tool_output, tool_call_id=tool_calls[0]['id']))

    output = llm_with_tools.invoke(messages)
    print(output.content)
    print(messages)

# https://github.com/projectwilsen/tool_calling_agent/blob/main/tool_calling.ipynb
