from base_agent import BaseSubAgent
from tools import get_weather


class WeatherAgent(BaseSubAgent):
    def __init__(self, model):
        super().__init__(
            name="weather_agent",
            description="Handles queries about the weather and temperature.",
            model=model,
            tools=[get_weather]
        )
