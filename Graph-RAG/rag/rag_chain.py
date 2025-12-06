from langchain_core.prompts import ChatPromptTemplate
from langchain_community.chat_models import ChatOllama
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

def get_rag_chain(retriever):
    llm = ChatOllama(model="llama3.1:8b")

    template = """
    You are a helpful assistant for Graph RAG.
    Context:
    {context}

    Question: {question}
    Answer concisely:
    """

    prompt = ChatPromptTemplate.from_template(template)

    chain = (
        {
            "context": retriever,
            "question": RunnablePassthrough(),
        }
        | prompt
        | llm
        | StrOutputParser()
    )
    return chain
