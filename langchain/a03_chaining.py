from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableLambda
from langchain_ollama import ChatOllama

llm = ChatOllama(
    model="llama3.2",
    temperature=0.2,
)

# full_chain = (
#         gen_haiku
#         | llm
#         | StrOutputParser()
#         | RunnableLambda(lambda haiku: {"input": haiku})
#         | select_words
#         | llm
#         | StrOutputParser()
# )

haiku_chain = ChatPromptTemplate.from_template("Write a short haiku from this input: {input}") | llm | StrOutputParser()
word_chain = ChatPromptTemplate.from_template("Select 5 words from this input: {input}") | llm | StrOutputParser()

# Full pipeline: input → haiku → 5 words
full_chain = haiku_chain | (lambda x: {"input": x}) | word_chain


if __name__ == "__main__":
    # Run the full pipeline
    input_text = "Balaton is the biggest lake in Hungary which is very popular at summer"
    result = full_chain.invoke({"input": input_text})
    print(result)
