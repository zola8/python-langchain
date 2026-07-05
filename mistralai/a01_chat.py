# quickstart.py
import os

from dotenv import load_dotenv
from mistralai.client import Mistral

load_dotenv()

client = Mistral(api_key=os.environ["MISTRAL_API_KEY"])

if __name__ == '__main__':
    response = client.chat.complete(
        model="mistral-large-latest",
        messages=[
            {"role": "user", "content": "What is Mistral AI?"}
        ],
    )

    print(response.choices[0].message.content)
