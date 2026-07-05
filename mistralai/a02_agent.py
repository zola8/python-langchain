# Synchronous Example
import os

from dotenv import load_dotenv
from mistralai.client import Mistral

load_dotenv()

if __name__ == '__main__':
    with Mistral(
        api_key=os.getenv("MISTRAL_API_KEY", ""),
    ) as mistral:
        res = mistral.agents.complete(messages=[
            {
                "role": "user",
                "content": "Who is the best French painter? Answer in one short sentence.",
            },
        ], agent_id="ag_019f278cf07571d89a5026e5fb4dec8c", stream=False, response_format={
            "type": "text",
        })

        # Handle response
        print(res)
        print(res.choices[0].message.content)
