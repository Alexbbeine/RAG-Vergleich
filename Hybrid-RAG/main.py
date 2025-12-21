from graph.neo4j_connector import get_graph
from graph.graph_builder import build_graph
from graph.vectorstore_builder import build_vectorstore
from rag.retriever import get_retriever
from rag.retriever import graph_retriever
from graph.create_index import index
from rag.rag_chain import get_rag_chain

def main():

    # 0. Graph-Objekt
    graph = get_graph()

    # 1. Graph-Daten aufbauen
    build_graph(graph, "dummytext.txt")

    # 2. Vectorstore
    vectorstore = build_vectorstore()

    # 3. Retriever
    retriever = get_retriever(vectorstore)

    # 4. Index kreieren
    index()

    # 5. Graph-Retriever
    print(graph_retriever(graph, "Who is Isabel?"))

    # 5. RAG Chain
    chain = get_rag_chain(graph, retriever)

    # Beispielanfragen
    question_1 = "Describe the structure of the Moreno family: who belongs to each generation, how they are related to each other, and where each nuclear family lives."
    print(chain.invoke(question_1))

    question_2 = "Describe the structure of the Moreno family: who belongs to each generation, how they are related to each other, and where each nuclear family lives."
    print(chain.invoke(question_2))

if __name__ == "__main__":
    main()
