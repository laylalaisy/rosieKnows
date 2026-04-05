# rosieKnows
Rosie knows everything! A production-style RAG knowledge system built with LLMs.

## Goals
- build an end-to-end RAG pipeline
- understand ingestion, retrieval, and generation
- explore evaluation and reliability

## Tech Stack
- Python
- FastAPI
- OpenAI / Claude
- Streamlit

## Logs
1. Retrieval: simple keywords intersection
2. Retrieval: update keywords with OpenAI embeddings model + consine similarity, each chunk calls `get_embedding` once now
3. Add embedding cache

## References
- Retrieval-Augmented Generation (RAG): https://www.pinecone.io/learn/retrieval-augmented-generation/
