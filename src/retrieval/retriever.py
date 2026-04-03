from typing import List, Tuple

def simple_keyword_retrieval(query: str, chunks: List[str], top_k: int = 3) -> List[Tuple[str, int]]:
    query_keywords = set(query.lower().split())
    scored_chunks = []

    for chunk in chunks:
        chunk_keywords = set(chunk.lower().split())
        score = len(query_keywords.intersection(chunk_keywords))
        scored_chunks.append((chunk, score))

    scored_chunks.sort(key=lambda x: x[1], reverse=True)
    return scored_chunks[:top_k]