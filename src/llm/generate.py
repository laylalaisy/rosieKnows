import os
from openai import OpenAI


def generate_answer(query: str, context_chunks: list[str]) -> str:
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("OPENAI_API_KEY is not set")

    client = OpenAI(api_key=api_key)

    context = "\n\n".join(context_chunks)

    prompt = f"""
You are a helpful assistant answering questions based only on the provided context.

Context:
{context}

Question:
{query}

Instructions:
- Answer using only the provided context.
- If the context is insufficient, say you do not know.
- Be concise.
"""

    response = client.responses.create(
        model="gpt-4.1-mini",
        input=prompt,
    )

    return response.output_text