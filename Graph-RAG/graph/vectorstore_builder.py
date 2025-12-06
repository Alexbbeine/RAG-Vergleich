from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Neo4jVector

def build_vectorstore(graph):
    embeddings = HuggingFaceEmbeddings(model_name="BAAI/bge-m3")
    vectorstore = Neo4jVector.from_existing_graph(
        embedding=embeddings,
        search_type="hybrid",
        node_label="Chunk",
        text_node_property="text",
        embedding_node_property="embedding"
    )
    return vectorstore
