from dataclasses import dataclass

from langchain.agents import create_agent
from langchain.agents.middleware import dynamic_prompt, ModelRequest
from langchain_ollama import ChatOllama


@dataclass
class Context:
    user_role: str
    deployment_env: str


@dynamic_prompt
def context_aware_prompt(request: ModelRequest) -> str:
    # Read from Runtime Context: user role and environment
    user_role = request.runtime.context.user_role
    env = request.runtime.context.deployment_env

    base = "You are a helpful assistant."

    if user_role == "admin":
        base += "\nYou have admin access. You can perform all operations."
    elif user_role == "viewer":
        base += "\nYou have read-only access. Guide users to read operations only."

    if env == "production":
        base += "\nBe extra careful with any data modifications."

    return base


llm = ChatOllama(model="llama3.2", temperature=0.2)  # llama3.2 - qwen3:4b

agent = create_agent(
    model=llm,
    tools=[],
    middleware=[context_aware_prompt],
    context_schema=Context
)

# https://docs.langchain.com/oss/python/langchain/context-engineering#system-prompt

if __name__ == "__main__":
    result = agent.invoke(
        {"messages": [{"role": "user", "content": "modify this content"}]},
        context=Context(user_role="viewer", deployment_env="dev")
    )

    print(result['messages'][-1].content)
