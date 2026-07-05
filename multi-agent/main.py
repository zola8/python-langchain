# main.py
import os

import uvicorn
from dotenv import load_dotenv
from fastapi import FastAPI
from langchain_mistralai import ChatMistralAI
from pydantic import BaseModel

from graph import AgentGraph
from manager_agent import ManagerAgent
from sub_agent_math import MathAgent
from sub_agent_search import SearchAgent
from sub_agent_weather import WeatherAgent

load_dotenv()

app = FastAPI(title="Multi-Agent Supervisor API")


class ChatRequest(BaseModel):
    message: str


class ChatResponse(BaseModel):
    response: str


llm = ChatMistralAI(
    model_name='mistral-large-latest',
    api_key=os.getenv('MISTRAL_API_KEY'),
    temperature=0.3,
    max_retries=2,
)

# 2. Instantiate Agents
weather_agent = WeatherAgent(llm)
math_agent = MathAgent(llm)
search_agent = SearchAgent(llm)
sub_agents = [weather_agent, math_agent, search_agent]

# 3. Instantiate Manager and Graph
manager = ManagerAgent(llm, sub_agents)
agent_graph = AgentGraph(manager, sub_agents)


@app.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    # Format input for LangGraph
    inputs = {"messages": [("user", request.message)]}

    # Invoke the graph
    result = agent_graph.invoke(inputs)

    # The last message in the state will be the final answer from the sub-agent
    final_message = result["messages"][-1].content

    return ChatResponse(response=final_message)


if __name__ == "__main__":
    print("http://127.0.0.1:8001/docs")
    uvicorn.run(app, host="0.0.0.0", port=8001)
