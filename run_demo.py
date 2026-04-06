import os
from dotenv import load_dotenv

from src.ingestion.loaders import load_text_file
from src.ingestion.chunker import chunk_text
from src.retrieval.index_builder import build_embedding_index
from src.retrieval.index_storage import load_index, save_index, index_exists
from src.retrieval.vector_retriever import retrieve_from_index
from src.llm.generate import generate_answer


def main():
    load_dotenv()

    file_path = "data/sample.txt"
    query = "What are the main components of Rosie Knows?"

    text = load_text_file(file_path)
    chunks = chunk_text(text, chunk_size=500, overlap=100)

    if index_exists():
        print("Loading existing index...")
        index = load_index()
    else:
        print("Building new index...")
        index = build_embedding_index(chunks)
        save_index(index)

    top_chunks_with_scores = retrieve_from_index(query, index, top_k=3)
    top_chunks = [chunk for chunk, _ in top_chunks_with_scores]

    print("=== Top Retrieved Chunks ===")
    for i, (chunk, score) in enumerate(top_chunks_with_scores, start=1):
        print(f"\n--- Chunk {i} | score={score} ---\n")
        print(chunk[:300])

    print("\n=== LLM Answer ===\n")
    answer = generate_answer(query, top_chunks)
    print(answer)


if __name__ == "__main__":
    main()