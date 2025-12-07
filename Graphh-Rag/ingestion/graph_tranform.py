from llm.llm_setup import llm
from ingestion.split_documents import documents
from langchain_experimental.graph_transformers import LLMGraphTransformer
from config import graph

llm_transformer = LLMGraphTransformer(llm=llm)
graph_documents = llm_transformer.convert_to_graph_documents(documents)

graph.add_graph_documents(
    graph_documents,
    baseEntityLabel=True,
    include_source=True
)
