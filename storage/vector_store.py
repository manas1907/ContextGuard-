import faiss
import numpy as np

class VectorStore:
    def __init__(self, dimension: int):
        self.index = faiss.IndexFlatIP(dimension)

    def add(self, vectors: np.ndarray):
        faiss.normalize_L2(vectors)
        self.index.add(vectors)

    def search(self, query_vector: np.ndarray, top_k: int):
        faiss.normalize_L2(query_vector)
        scores, indices = self.index.search(query_vector, top_k)
        return scores[0], indices[0]
