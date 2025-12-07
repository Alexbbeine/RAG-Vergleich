from langchain_community.vectorstores import Neo4jVector
from embeddings.embedding_model import embeddings

vector_index = Neo4jVector.from_existing_graph(
    embeddings,
    search_type="hybrid",
    node_label="Document",
    text_node_properties=["text"],
    embedding_node_property="embedding",
    url="bolt://neo4j:7687",
    username="neo4j",
    password="ps_neo4jj",
)

vector_retriever = vector_index.as_retriever()
