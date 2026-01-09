from dataclasses import dataclass
from typing import Literal

from langchain.agents import create_agent
from langchain.agents.structured_output import ToolStrategy
from langchain_ollama import ChatOllama


@dataclass
class ProductReview:
    """Analysis of a product review."""
    rating: int | None  # The rating of the product (1-5)
    sentiment: Literal["positive", "negative"]  # The sentiment of the review
    key_points: list[str]  # The key points of the review


llm = ChatOllama(model="qwen3:4b", temperature=0.2)  # llama3.2 - qwen3:4b

agent = create_agent(
    model=llm,
    tools=[],
    response_format=ToolStrategy(ProductReview)
)

if __name__ == "__main__":
    result = agent.invoke({
        "messages": [
            {
                "role": "user",
                "content": "Analyze this review: 'Great product: 5 out of 5 stars. Fast shipping, but expensive'"
            }
        ]
    })
    print(result["structured_response"])

    # ProductReview(rating=5, sentiment='positive', key_points=['Fast shipping', 'expensive'])
