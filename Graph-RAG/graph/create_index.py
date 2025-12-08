from neo4j import GraphDatabase
from config.settings import NEO4J_URI, NEO4J_USERNAME, NEO4J_PASSWORD

driver = GraphDatabase.driver(
    uri=NEO4J_URI,
    auth=(NEO4J_USERNAME, NEO4J_PASSWORD)
)

def create_fulltext_index(tx):
    query = '''
    CREATE FULLTEXT INDEX `fulltext_entity_id` 
    FOR (n:__Entity__) 
    ON EACH [n.id];
    '''
    tx.run(query)

# Function to execute the query
def create_index():
    with driver.session() as session:
        session.execute_write(create_fulltext_index)
        print("Fulltext index created successfully.")

def index():
    try:
        create_index()
    except Exception as e:
        print("Index creation failed:", e)
    finally:
        driver.close()
