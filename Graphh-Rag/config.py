from dotenv import load_dotenv
from langchain_neo4j import Neo4jGraph

load_dotenv()

graph = Neo4jGraph(
    url="bolt://neo4j:7687",
    username="neo4j",
    password="ps_neo4jj"
)
