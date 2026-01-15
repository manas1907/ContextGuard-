from ingestion.loader import load_text_file
from processing.chunker import chunk_text
from processing.embedder import Embedder
from storage.vector_store import VectorStore
from retrieval.retriever import Retriever
from validation.validator import EvidenceValidator
from reasoning.generator import AnswerGenerator
from config import TOP_K
from utils.logger import log

def build_context_guard(document_path: str):
    log("Loading document")
    document = load_text_file(document_path)

    log("Chunking document")
    chunks = chunk_text(document)

    log("Embedding chunks")
    embedder = Embedder()
    embeddings = embedder.embed(chunks)

    log("Building vector store")
    store = VectorStore(embeddings.shape[1])
    store.add(embeddings)

    retriever = Retriever(store, chunks, embedder)
    validator = EvidenceValidator()
    generator = AnswerGenerator()

    return retriever, validator, generator

if __name__ == "__main__":
    retriever, validator, generator = build_context_guard("document.txt")

    while True:
        question = input("\nAsk question (or exit): ")
        if question.lower() == "exit":
            break

        retrieved = retriever.retrieve(question, TOP_K)
        validation = validator.validate(retrieved)

        if not validation["valid"]:
            print({
                "status": "REFUSED",
                "reason": validation["reason"],
                "confidence": validation["confidence"]
            })
            continue

        answer = generator.generate(question, retrieved)

        print({
            "status": "ANSWERED",
            "answer": answer,
            "confidence": validation["confidence"]
        })
