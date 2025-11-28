from typing import Optional
from pydantic import BaseModel


class AddDocumentRequest(BaseModel):
    title: str
    content: str


class UpdateDocumentRequest(BaseModel):
    title: str
    content: str


class SearchRequest(BaseModel):
    query: str
    n_results: Optional[int] = 5


class DocumentResponse(BaseModel):
    status: str
    id: str
    message: Optional[str] = None


class SearchResult(BaseModel):
    id: str
    title: str
    content: str
    distance: Optional[float] = None


class DocumentListItem(BaseModel):
    id: str
    title: str
    content: str
    hash: str


