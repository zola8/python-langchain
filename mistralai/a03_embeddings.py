# Synchronous Example
import os

from dotenv import load_dotenv
from mistralai.client import Mistral

load_dotenv()

if __name__ == '__main__':

    with Mistral(
        api_key=os.getenv("MISTRAL_API_KEY", ""),
    ) as mistral:
        res = mistral.embeddings.create(model="mistral-embed", inputs=[
            "Embed this sentence.",
            "As well as this one.",
        ])

        # Handle response
        print(res)
