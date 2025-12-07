from langchain_experimental.graph_transformers import LLMGraphTransformer
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import TextLoader
from langchain_community.chat_models import ChatOllama
from langchain_experimental.llms.ollama_functions import OllamaFunctions


def build_graph(graph, input_file: str):
    loader = TextLoader(input_file)
    docs = loader.load()

    splitter = RecursiveCharacterTextSplitter(chunk_size=250, chunk_overlap=24)
    chunks = splitter.split_documents(docs)

    llm = OllamaFunctions(model="llama3.1:8b", temperature=0, format="json", base_url="http://ollama:11434")

    transformer = LLMGraphTransformer(llm=llm)
    graph_documents = transformer.convert_to_graph_documents(chunks)
    graph_documents[0]

    graph.add_graph_documents(graph_documents, baseEntityLabel=True, include_source=True)
