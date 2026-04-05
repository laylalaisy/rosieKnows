## Outputs with Embedding Cache
Building embedding index...
=== Top Retrieved Chunks ===

--- Chunk 1 | score=0.6351963371589886 ---

Rosie Knows Project Overview

Rosie Knows is a production-style LLM knowledge platform designed to help users query and understand information from a collection of documents using Retrieval-Augmented Generation (RAG).

The system is built as a learning project for AI platform engineering. It focuses

--- Chunk 2 | score=0.5672351331469192 ---

ing keyword and vector search
- caching for faster query responses
- evaluation pipelines for measuring answer quality
- support for different document formats such as PDFs
- deployment as a web service

Conclusion

Rosie Knows is not just a demo application, but a system designed to reflect real AI

--- Chunk 3 | score=0.29529491768733995 ---

n, and evaluation.

System Architecture

The system is composed of several core components:

1. Ingestion Pipeline
The ingestion pipeline is responsible for loading documents, parsing their content, and splitting them into smaller chunks. These chunks are later used for retrieval.

2. Embedding Laye

=== LLM Answer ===

The main components of Rosie Knows are:

1. Ingestion Pipeline - loads, parses, and splits documents into chunks.
2. Embedding Layer - transforms chunks into vector representations.
3. Vector Storage - stores all embeddings for retrieval.