from typing import List, Dict, Any
from src.embeddings.embedder import get_embedding


def build_embedding_index(chunks: List[str]) -> List[Dict[str, Any]]:
    index = []

    for i, chunk in enumerate(chunks):
        embedding = get_embedding(chunk)
        index.append(
            {
                "chunk_id": i,
                "text": chunk,
                "embedding": embedding,
            }
        )

    return index