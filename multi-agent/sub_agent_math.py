from base_agent import BaseSubAgent
from tools import calculate_math


class MathAgent(BaseSubAgent):
    def __init__(self, model):
        super().__init__(
            name="math_agent",
            description="Handles mathematical calculations and expressions.",
            model=model,
            tools=[calculate_math]
        )
