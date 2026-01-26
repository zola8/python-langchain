from pprint import pprint

import requests

BASE_URL = "http://localhost:11434/api"


def get_ollama_models() -> list:
    response = requests.get(BASE_URL + "/tags")
    return response.json()["models"]


if __name__ == '__main__':
    ollama_models = get_ollama_models()
    pprint(ollama_models)
