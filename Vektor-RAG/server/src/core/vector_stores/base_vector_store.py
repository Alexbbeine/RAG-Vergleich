from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any
from ..document import Document


class BaseVectorStore(ABC):
    @abstractmethod
    def add_document(self, document: Document, embedding: List[float]) -> str:
        """Add a document with its embedding. Returns the document ID."""
        pass

    @abstractmethod
    def update_document(self, doc_id: str, document: Document, embedding: List[float]) -> bool:
        """Update an existing document. Returns True if successful."""
        pass

    @abstractmethod
    def delete_document(self, doc_id: str) -> bool:
        """Delete a document by ID. Returns True if successful."""
        pass

    @abstractmethod
    def search(self, query_embedding: List[float], n_results: int = 5) -> List[Dict[str, Any]]:
        """Search for similar documents. Returns list of documents with metadata."""
        pass

    @abstractmethod
    def get_document_by_hash(self, document_hash: str) -> Optional[str]:
        """Find document ID by content hash. Returns doc_id if found, None otherwise."""
        pass

    @abstractmethod
    def get_all_documents(self) -> List[Dict[str, Any]]:
        """Get all documents in the store. Returns list of documents with metadata."""
        pass