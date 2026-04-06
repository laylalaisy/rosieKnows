from typing import List, Dict, Any
from src.embeddings.embedder import get_embedding


def build_embedding_index(
        chunks: List[str],
        document_id: str,
        source_name:str
) -> List[Dict[str, Any]]:
    index = []

    for i, chunk in enumerate(chunks):
        embedding = get_embedding(chunk)
        index.append(
            {
                "chunk_id": f"{document_id}_{i}",
                "document_id": document_id,
                "source": source_name,
                "chunk_index": i,
                "text": chunk,
                "embedding": embedding,
            }
        )

    return index