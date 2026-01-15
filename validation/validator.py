from config import SIMILARITY_THRESHOLD

class EvidenceValidator:
    def validate(self, retrieved_chunks: list[dict]) -> dict:
        best_score = retrieved_chunks[0]["score"]

        if best_score < SIMILARITY_THRESHOLD:
            return {
                "valid": False,
                "confidence": best_score,
                "reason": "Insufficient semantic evidence in document"
            }

        return {
            "valid": True,
            "confidence": best_score
        }
