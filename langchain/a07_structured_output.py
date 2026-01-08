from langchain_ollama import ChatOllama
from pydantic import BaseModel, Field


class Movie(BaseModel):
    title: str = Field(description="The title of the movie")
    year: int = Field(description="This year the movie was released")
    director: str = Field(description="The director of the movie")
    rating: float = Field(description="The movies rating out of 10")


llm = ChatOllama(model="qwen3:4b", temperature=0.2)

model_with_structure = llm.with_structured_output(Movie)

if __name__ == "__main__":
    result = llm.invoke("Provide brief details about Terminator")
    print(result)

    result = model_with_structure.invoke("Provide details about Terminator")
    print(result)

# Here\'s a concise overview of the **Terminator** franchise:\n\n1.  **Origin**: The term "Terminator" refers to **cyborg assassins**
# (like the iconic T-800 model) created by **Skynet** (a self-aware AI) to eliminate humanity, specifically **Sarah Connor** (a future resistance leader).\n2.
# **Core Concept**: The franchise centers on **time travel**—a future Terminator (from 2029) is sent back to 1984 to kill Sarah Connor before
# she becomes the key to stopping Skynet. The T-800 is a highly advanced, human-like robot designed for this mission.\n3.
# **Key Film**: The 1984 film *Terminator* (directed by James Cameron) is the origin story.
# It established the franchise\'s iconic themes: AI rebellion, human resistance, and the high-stakes battle between technology and survival.\n4.
# **Franchise Scope**: While the 1984 film is the foundation, the franchise includes sequels (*Terminator 2: Judgment Day*, 1991),
# TV series (*Terminator: The Sarah Connor Chronicles*), and newer films (*Terminator: Dark Fate*, 2019).\n\n
# **In one sentence**: *Terminator* is a sci-fi action franchise where a future AI (Skynet) sends a cyborg assassin (the T-800) back in time
# to kill a woman who will stop the AI\'s takeover of Earth—most famously launched by the 1984 film.'

# title='Terminator: A Comprehensive Overview of the Franchise' year=2023 director='Alexis C. Arquette' rating=4.85
