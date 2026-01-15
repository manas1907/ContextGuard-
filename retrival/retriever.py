class Retriever:
    def __init__(self, vector_store, chunks, embedder):
        self.vector_store = vector_store
        self.chunks = chunks
        self.embedder = embedder

    def retrieve(self, query: str, top_k: int):
        query_vector = self.embedder.embed([query])
        scores, indices = self.vector_store.search(query_vector, top_k)

        results = []
        for score, idx in zip(scores, indices):
            results.append({
                "text": self.chunks[idx],
                "score": float(score)
            })

        return results
