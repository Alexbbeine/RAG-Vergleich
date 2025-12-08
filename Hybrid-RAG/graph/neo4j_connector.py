import time
from neo4j import GraphDatabase, exceptions as neo4j_exceptions
from langchain_neo4j import Neo4jGraph
from config.settings import NEO4J_URI, NEO4J_USERNAME, NEO4J_PASSWORD

def wait_for_neo4j(max_retries: int = 20, delay_seconds: int = 5) -> None:
    """
    Wartet, bis Neo4j erreichbar ist, oder wirft nach `max_retries` eine Exception.
    Nutzt den offiziellen Neo4j-Treiber mit einem kleinen Test-Query.
    """
    print(f"Waiting for Neo4j at {NEO4J_URI} ...")
    driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USERNAME, NEO4J_PASSWORD))
    try:
        for attempt in range(1, max_retries + 1):
            try:
                with driver.session() as session:
                    session.run("RETURN 1 AS ok")
                print("Neo4j ist erreichbar.")
                return
            except neo4j_exceptions.ServiceUnavailable as e:
                print(f"[{attempt}/{max_retries}] Neo4j noch nicht bereit: {e}")
                if attempt == max_retries:
                    raise RuntimeError("Neo4j wurde nicht rechtzeitig erreichbar.") from e
                time.sleep(delay_seconds)
    finally:
        driver.close()


def get_graph() -> Neo4jGraph:
    """
    Wartet erst auf Neo4j und gibt dann ein Neo4jGraph-Objekt zurück.
    """
    wait_for_neo4j()
    return Neo4jGraph(
        url=NEO4J_URI,
        username=NEO4J_USERNAME,
        password=NEO4J_PASSWORD,
    )