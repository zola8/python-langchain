import os

from dotenv import load_dotenv
from langchain_classic.agents import create_react_agent, AgentExecutor
from langchain_core.prompts import PromptTemplate
from langchain_mistralai import ChatMistralAI

load_dotenv()

llm = ChatMistralAI(
    model_name='mistral-large-latest',
    api_key=os.getenv('MISTRAL_API_KEY'),
    temperature=0.3,
    max_retries=2,
)

template = '''Answer the following questions as best you can. You have access to the following tools:

{tools}

Use the following format:

Question: the input question you must answer
Thought: you should always think about what to do
Action: the action to take, should be one of [{tool_names}]
Action Input: the input to the action
Observation: the result of the action
... (this Thought/Action/Action Input/Observation can repeat N times)
Thought: I now know the final answer
Final Answer: the final answer to the original input question

Begin!

Question: {input}
Thought:{agent_scratchpad}'''

prompt = PromptTemplate.from_template(template)

tools = []

agent = create_react_agent(
    llm=llm,
    tools=tools,
    prompt=prompt,
)

# The AgentExecutor is responsible for running the agent with the provided tools.
agent_executor = AgentExecutor(
    agent=agent,
    tools=tools,
    verbose=True,
    handle_parsing_errors=True
)

if __name__ == '__main__':
    result = agent_executor.invoke({"input": "What's 5 + 3, then multiply by 2"})
    print("\nResult:")
    print(result["output"])
