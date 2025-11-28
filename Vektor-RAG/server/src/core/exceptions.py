class DocumentAlreadyExistsError(Exception):
    def __init__(self, doc_id: str):
        self.doc_id = doc_id
        super().__init__(f"Document already exists with ID: {doc_id}")


class DocumentNotFoundError(Exception):
    def __init__(self, doc_id: str):
        self.doc_id = doc_id
        super().__init__(f"Document not found with ID: {doc_id}")


class DocumentUpdateError(Exception):
    def __init__(self, doc_id: str):
        self.doc_id = doc_id
        super().__init__(f"Failed to update document with ID: {doc_id}")


class DocumentDeleteError(Exception):
    def __init__(self, doc_id: str):
        self.doc_id = doc_id
        super().__init__(f"Failed to delete document with ID: {doc_id}")