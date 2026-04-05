# rosieKnows
Rosie (my 4yo Corgi) knows everything xD

This project is trying to build a  production-style (hopefully) RAG knowledge system for fun!

## Goals
- Build an end-to-end RAG pipeline
- Understand ingestion, retrieval, and generation etc
- Explore evaluation and reliability

## Tech Stack
- Python
- FastAPI
- OpenAI / Claude
- Streamlit

## Logs
3. Add embedding cache to precompute embedding index + query-time retrieval over cached vectors
2. Retrieval: update keywords with OpenAI embeddings model + consine similarity, each chunk calls `get_embedding` once now
1. Retrieval: simple keywords intersection

## References
- Retrieval-Augmented Generation (RAG): https://www.pinecone.io/learn/retrieval-augmented-generation/
