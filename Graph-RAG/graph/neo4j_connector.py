from langchain_neo4j import Neo4jGraph
from config.settings import NEO4J_URI, NEO4J_USERNAME, NEO4J_PASSWORD

def get_graph():
    return Neo4jGraph(
        url=NEO4J_URI,
        username=NEO4J_USERNAME,
        password=NEO4J_PASSWORD
    )
