from typing import List, Tuple
from src.embeddings.embedder import get_embedding
from src.retrieval.vector_utils import cosine_similarity


def retrieve_with_embeddings(
    query: str,
    chunks: List[str],
    top_k: int = 3
) -> List[Tuple[str, float]]:
    query_emb = get_embedding(query)

    scored = []
    for chunk in chunks:
        chunk_emb = get_embedding(chunk)
        score = cosine_similarity(query_emb, chunk_emb)
        scored.append((chunk, score))

    scored.sort(key=lambda x: x[1], reverse=True)

    return scored[:top_k]