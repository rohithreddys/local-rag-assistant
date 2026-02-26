# Local RAG Assistant (100% Free)

A fully local Retrieval-Augmented Generation (RAG) system built using:

- Ollama (llama3)
- HuggingFace embeddings
- Chroma vector database
- LangChain
- Gradio UI

## Features

- PDF ingestion
- Semantic chunking
- Vector storage
- Context-based answer generation
- Fully local (no API cost)

## Setup

1. Install Ollama  
2. Pull llama3 model:
   ollama pull llama3

3. Install dependencies:
   pip install -r requirements.txt

4. Run ingestion:
   python rag/ingest.py

5. Launch app:
   python app.py

## Adding Documents

This repository does not include sample documents.

To add your own PDF:

1. Create a folder named `data/`
2. Add your PDF file inside:
   data/sample.pdf
3. Run ingestion:
   python rag/ingest.py

The vector embeddings will be stored locally in the `vectorstore/` directory.