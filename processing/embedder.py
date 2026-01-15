import numpy as np
from sentence_transformers import SentenceTransformer
from config import EMBED_MODEL_NAME

class Embedder:
    def __init__(self):
        self.model = SentenceTransformer(EMBED_MODEL_NAME)

    def embed(self, texts: list[str]) -> np.ndarray:
        embeddings = self.model.encode(texts, convert_to_numpy=True)
        return embeddings
