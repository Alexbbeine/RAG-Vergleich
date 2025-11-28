from .base_vector_store import BaseVectorStore
from ..document import Document
import uuid
from typing import List, Optional, Dict, Any
import chromadb


class ChromaVectorStore(BaseVectorStore):
    def __init__(self, collection_name: str = "documents"):
        self.client = chromadb.Client()
        self.collection = self.client.create_collection(
            name=collection_name,
            get_or_create=True
        )

    def add_document(self, document: Document, embedding: List[float]) -> str:
        doc_id = str(uuid.uuid4())

        self.collection.add(
            documents=[document.content],
            embeddings=[embedding],
            metadatas=[{
                "title": document.title,
                "hash": document.hash
            }],
            ids=[doc_id]
        )
        return doc_id

    def update_document(self, doc_id: str, document: Document, embedding: List[float]) -> bool:
        try:
            self.collection.update(
                ids=[doc_id],
                documents=[document.content],
                embeddings=[embedding],
                metadatas=[{
                    "title": document.title,
                    "hash": document.hash
                }]
            )
            return True
        except Exception:
            return False

    def delete_document(self, doc_id: str) -> bool:
        try:
            self.collection.delete(ids=[doc_id])
            return True
        except Exception:
            return False

    def search(self, query_embedding: List[float], n_results: int = 5) -> List[Dict[str, Any]]:
        results = self.collection.query(
            query_embeddings=[query_embedding],
            n_results=n_results
        )

        documents = []
        for i in range(len(results["ids"][0])):
            documents.append({
                "id": results["ids"][0][i],
                "title": results["metadatas"][0][i]["title"],
                "content": results["documents"][0][i],
                "distance": results["distances"][0][i] if "distances" in results else None
            })

        return documents

    def get_document_by_hash(self, document_hash: str) -> Optional[str]:
        results = self.collection.get(
            where={"hash": document_hash}
        )

        if results["ids"]:
            return results["ids"][0]
        return None

    def get_all_documents(self) -> List[Dict[str, Any]]:
        results = self.collection.get()

        documents = []
        for i in range(len(results["ids"])):
            documents.append({
                "id": results["ids"][i],
                "title": results["metadatas"][i]["title"],
                "content": results["documents"][i],
                "hash": results["metadatas"][i]["hash"]
            })

        return documents