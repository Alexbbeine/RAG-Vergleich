from neo4j import GraphDatabase

driver = GraphDatabase.driver(
    uri="bolt://neo4j:7687",
    auth=("neo4j", "ps_neo4jj")
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

try:
    create_index()
except Exception as e:
    print("Index creation failed:", e)

driver.close()
