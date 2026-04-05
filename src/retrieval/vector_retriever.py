from typing import List, Tuple, Dict, Any
from src.embeddings.embedder import get_embedding
from src.retrieval.vector_utils import cosine_similarity

def retrieve_from_index(
    query: str,
    index: List[Dict[str, Any]],
    top_k: int = 3
) -> List[Tuple[str, float]]:
    query_emb = get_embedding(query)

    scored = []
    for item in index:
        score = cosine_similarity(query_emb, item["embedding"])
        scored.append((item["text"], score))

    scored.sort(key=lambda x: x[1], reverse=True)

    return scored[:top_k]