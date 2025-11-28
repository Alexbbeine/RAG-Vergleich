from .base_embedder import BaseEmbedder
from typing import List
import torch
from sentence_transformers import SentenceTransformer


class SentenceTransformerEmbedder(BaseEmbedder):
    def __init__(self, model_name: str):
        device = 'cuda' if torch.cuda.is_available() else 'cpu'

        self.model = SentenceTransformer(model_name, device=device)
        print(f"SentenceTransformer loaded on device: {device}")

        if device == 'cuda':
            print(f"GPU: {torch.cuda.get_device_name(0)}")

    def embed(self, text: str) -> List[float]:
        embedding = self.model.encode(text)
        return embedding.tolist()