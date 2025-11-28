from .base_embedder import BaseEmbedder
from openai import AzureOpenAI
from typing import List


class AzureOpenAIEmbedder(BaseEmbedder):
    def __init__(self, model_name: str):
        self.model_name = model_name
        self.client = AzureOpenAI()

    def embed(self, text: str) -> List[float]:
        response = self.client.embeddings.create(
            input=text,
            model=self.model_name
        )
        return response.data[0].embedding
