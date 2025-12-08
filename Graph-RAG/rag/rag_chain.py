from langchain_core.prompts import ChatPromptTemplate
from langchain_community.chat_models import ChatOllama
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from rag.retriever import full_retriever

def get_rag_chain():
    llm = ChatOllama(model="llama3.1:8b", temperature=0, format="json", base_url="http://ollama:11434")

    template = """
    You are a helpful assistant for Graph RAG.
    Context:
    {context}

    Question: {question}
    Answer concisely:
    """

    prompt = ChatPromptTemplate.from_template(template)

    def context_fn(question: str) -> str:
        return full_retriever(graph, retriever, question)
    
    chain = (
        {
            "context": context_fn,
            "question": RunnablePassthrough(),
        }
        | prompt
        | llm
        | StrOutputParser()
    )
    return chain
