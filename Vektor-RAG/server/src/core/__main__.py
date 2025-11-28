from fastmcp import settings
from fastmcp import FastMCP
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from typing import List
import uvicorn

from .rag_service import RAGService
from .embedders.sentence_transformer_embedder import SentenceTransformerEmbedder
from .vector_stores.chroma_vector_store import ChromaVectorStore
from .schemas import AddDocumentRequest, UpdateDocumentRequest, SearchRequest, DocumentResponse, SearchResult, DocumentListItem
from .exceptions import DocumentAlreadyExistsError, DocumentUpdateError, DocumentDeleteError

settings.stateless_http = True
mcp = FastMCP(name="RAG Framework", instructions="Simple RAG framework with document indexing and search")
mcp_app = mcp.http_app()
app = FastAPI(lifespan=mcp_app.lifespan)

# Initialize RAG service
embedder = SentenceTransformerEmbedder("BAAI/bge-m3")
vector_store = ChromaVectorStore("documents")
rag_service = RAGService(embedder, vector_store)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # For development - restrict in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@mcp.tool()
def search(query: str, n_results: int = 5) -> List[SearchResult]:
    """Search for documents in the RAG index"""
    results = rag_service.search(query, n_results)
    return [SearchResult(**result) for result in results]


@app.post("/search", response_model=List[SearchResult])
def search(request: SearchRequest):
    """Search for documents in the RAG index"""
    results = rag_service.search(request.query, request.n_results)
    return [SearchResult(**result) for result in results]


@app.post("/documents", response_model=DocumentResponse)
def add_document(request: AddDocumentRequest):
    """Add a new document to the index"""
    try:
        doc_id = rag_service.add_document(request.title, request.content)
        return DocumentResponse(status="added", id=doc_id)
    except DocumentAlreadyExistsError as e:
        return DocumentResponse(status="exists", id=e.doc_id, message="Document already exists")


@app.put("/documents/{doc_id}", response_model=DocumentResponse)
def update_document(doc_id: str, request: UpdateDocumentRequest):
    """Update an existing document"""
    try:
        rag_service.update_document(doc_id, request.title, request.content)
        return DocumentResponse(status="updated", id=doc_id)
    except DocumentUpdateError as e:
        return DocumentResponse(status="error", id=e.doc_id, message="Document not found or update failed")


@app.delete("/documents/{doc_id}", response_model=DocumentResponse)
def delete_document(doc_id: str):
    """Delete a document from the index"""
    try:
        rag_service.delete_document(doc_id)
        return DocumentResponse(status="deleted", id=doc_id)
    except DocumentDeleteError as e:
        return DocumentResponse(status="error", id=e.doc_id, message="Document not found or deletion failed")


@app.get("/documents", response_model=List[DocumentListItem])
def get_all_documents():
    """Get all documents in the index"""
    documents = rag_service.get_all_documents()
    return [DocumentListItem(**doc) for doc in documents]


@app.get("/health")
def health_check():
    return {"server": "running"}


@app.options("/{path:path}", status_code=204)
def preflight(path: str):
    return ""


def main():
    app.mount("/", mcp_app)
    uvicorn.run(app, host="0.0.0.0", port=8000)


if __name__ == "__main__":
    main()
