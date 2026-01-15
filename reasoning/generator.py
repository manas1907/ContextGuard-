from openai import OpenAI
from config import LLM_MODEL

class AnswerGenerator:
    def __init__(self):
        self.client = OpenAI()

    def generate(self, question: str, evidence_chunks: list[dict]) -> str:
        evidence_text = "\n\n".join(
            [chunk["text"] for chunk in evidence_chunks]
        )

        prompt = f"""
You are a strict document-based AI.

Rules:
- Answer ONLY from the evidence
- If answer is missing, reply exactly: NOT FOUND
- Do not guess
- Do not add external knowledge

Evidence:
{evidence_text}

Question:
{question}
"""

        response = self.client.chat.completions.create(
            model=LLM_MODEL,
            temperature=0,
            messages=[{"role": "user", "content": prompt}]
        )

        return response.choices[0].message.content.strip()
