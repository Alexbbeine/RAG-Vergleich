from typing import List, Dict, Any
from .document import Document
from .embedders.base_embedder import BaseEmbedder
from .vector_stores.base_vector_store import BaseVectorStore
from .exceptions import DocumentAlreadyExistsError, DocumentUpdateError, DocumentDeleteError


class RAGService:
    def __init__(self, embedder: BaseEmbedder, vector_store: BaseVectorStore):
        self.embedder = embedder
        self.vector_store = vector_store

    def add_document(self, title: str, content: str) -> str:
        document = Document(title, content)

        # Check for duplicates
        existing_id = self.vector_store.get_document_by_hash(document.hash)
        if existing_id:
            raise DocumentAlreadyExistsError(existing_id)

        # Generate embedding and add document
        embedding = self.embedder.embed(f"{title}\n\n{content}")
        doc_id = self.vector_store.add_document(document, embedding)

        return doc_id

    def update_document(self, doc_id: str, title: str, content: str) -> None:
        document = Document(title, content)
        embedding = self.embedder.embed(f"{title}\n\n{content}")

        success = self.vector_store.update_document(doc_id, document, embedding)
        if not success:
            raise DocumentUpdateError(doc_id)

    def delete_document(self, doc_id: str) -> None:
        success = self.vector_store.delete_document(doc_id)
        if not success:
            raise DocumentDeleteError(doc_id)

    def search(self, query: str, n_results: int = 5) -> List[Dict[str, Any]]:
        query_embedding = self.embedder.embed(query)
        return self.vector_store.search(query_embedding, n_results)

    def get_all_documents(self) -> List[Dict[str, Any]]:
        return self.vector_store.get_all_documents()
