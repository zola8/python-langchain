import json
import os

from dotenv import load_dotenv
from mistralai.client import Mistral

load_dotenv()

client = Mistral(api_key=os.environ["MISTRAL_API_KEY"])

# Define the tool schema
tools = [
    {
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "Get the current weather for a given city.",
            "parameters": {
                "type": "object",
                "properties": {
                    "city": {
                        "type": "string",
                        "description": "The city name, e.g. 'Paris'."
                    }
                },
                "required": ["city"]
            }
        }
    }
]


# Simulate the function (replace with a real API call)
def get_weather(city: str) -> dict:
    return {"city": city, "temperature": "18°C", "condition": "Partly cloudy"}



if __name__ == '__main__':
    messages = [
        {"role": "user", "content": "What's the weather in Paris today?"}
    ]

    response = client.chat.complete(
        model="mistral-medium-latest",
        messages=messages,
        tools=tools,
    )

    tool_call = response.choices[0].message.tool_calls[0]
    print(f"Model wants to call: {tool_call.function.name}")
    print(f"With arguments: {tool_call.function.arguments}")

    # Execute the tool call
    args = json.loads(tool_call.function.arguments)
    result = get_weather(**args)

    # Send the result back to the model
    messages.append(response.choices[0].message)
    messages.append({
        "role": "tool",
        "name": tool_call.function.name,
        "content": json.dumps(result),
        "tool_call_id": tool_call.id,
    })

    final_response = client.chat.complete(
        model="mistral-medium-latest",
        messages=messages,
        tools=tools,
    )
    messages.append(final_response.choices[0].message)

    print(final_response.choices[0].message.content)
    # "The weather in Paris is 18°C and partly cloudy."

    print("-" * 20)
    for msg in messages:
        print(f"Message: {msg}")
