import uvicorn
from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama import ChatOllama

app = FastAPI()

llm = ChatOllama(model="llama3.2", temperature=0.2)
prompt = ChatPromptTemplate.from_template(
    "You are a helpful assistant. Answer as short as possible. The question: {question}")
chain = prompt | llm


@app.get("/", tags=["ask"])
def ask(question: str | None = None) -> str:
    answer = chain.invoke({"question": question})
    print(f"Question: {question}\nAnswer: {answer}")
    return answer.content


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8080)
