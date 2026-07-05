import os
import uuid

from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_mistralai import ChatMistralAI
from langgraph.checkpoint.memory import InMemorySaver

load_dotenv()

llm = ChatMistralAI(
    model_name='mistral-large-latest',
    api_key=os.getenv('MISTRAL_API_KEY'),
    temperature=0.3,
    max_retries=2,
)

agent = create_agent(
    model=llm,
    tools=[],
    checkpointer=InMemorySaver(),
)

config = {"configurable": {"thread_id": str(uuid.uuid4())}}

if __name__ == '__main__':
    result = agent.invoke(
        {"messages": [{"role": "user", "content": "Who is Harry Potter?"}]},
        config=config,
    )

    # A follow-up turn on the same conversation: reuse the same thread_id to keep history
    result = agent.invoke(
        {"messages": [{"role": "user", "content": "How old is he?"}]},
        config=config,
    )

    for msg in result["messages"]:
        print(f"\n{'=' * 60}")
        print(f"Role: {msg.type.upper()}")
        print(f"{'-' * 60}")
        print(msg.content)
