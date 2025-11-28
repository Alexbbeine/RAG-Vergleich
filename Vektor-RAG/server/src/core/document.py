import hashlib


class Document:
    def __init__(self, title: str, content: str):
        self.title = title
        self.content = content

    @property
    def hash(self) -> str:
        return hashlib.sha256(f"{self.title}|{self.content}".encode()).hexdigest()