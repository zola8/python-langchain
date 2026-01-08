from typing import TypedDict, Annotated

from langchain_ollama import ChatOllama


# https://github.com/krishnaik06/Langchain-V1-Crash-Course/blob/main/updatedlangchain/5-structuredoutput.ipynb

# TypedDict provides a simpler alternative using Python’s built-in typing, ideal when you don’t need runtime validation.

class Actor(TypedDict):
    name: str
    role: str


class Movie(TypedDict):
    """A movie with details."""
    title: Annotated[str, ..., "The title of the movie"]
    year: Annotated[int, ..., "The year the movie was released"]
    cast: list[Actor]
    director: Annotated[str, ..., "The director of the movie"]
    rating: Annotated[float, ..., "The movie's rating out of 10"]


llm = ChatOllama(model="qwen3:4b", temperature=0.2)

model_with_typedict = llm.with_structured_output(Movie)

if __name__ == "__main__":
    result = model_with_typedict.invoke("Provide details about Terminator")
    print(result)

# {
#    "title":"Terminator: A Comprehensive Overview",
#    "year":1984,
#    "cast":[
#       {
#          "name":"Arnold Schwarzenegger",
#          "role":"T-800"
#       },
#       {
#          "name":"Mary Elizabeth Winstead",
#          "role":"Sarah Connor"
#       },
#       {
#          "name":"Michael B. Jordan",
#          "role":"Kyle Reese"
#       }
#    ],
#    "director":"James Cameron",
#    "rating":4.5
# }
