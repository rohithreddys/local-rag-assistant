# 🧠 Local Multi-Document RAG Assistant (100% Free)

A fully local Retrieval-Augmented Generation (RAG) system built using:

- 🦙 Ollama (Llama 3)
- 🤗 HuggingFace Embeddings (all-MiniLM-L6-v2)
- 📦 Chroma Vector Database (persistent)
- 🔗 LangChain (LCEL pipeline)
- 🎨 Gradio UI

This project supports **multi-PDF ingestion** and **source-aware responses** — all without any API costs.

---

## 🚀 Features

- ✅ Fully local LLM (llama3 via Ollama)
- ✅ Local embedding model (no API usage)
- ✅ Persistent vector database (Chroma)
- ✅ Multi-document PDF ingestion
- ✅ Source file attribution in responses
- ✅ Modular architecture (retriever + LLM separated)
- ✅ Zero cloud dependency
- ✅ GitHub-safe project structure

---

## 🏗 Architecture

User Question
↓
Retriever (Chroma)
↓
Top Relevant Chunks (from multiple PDFs)
↓
Prompt Construction
↓
Llama3 via Ollama
↓
Grounded Answer + Source Files

This design cleanly separates:

- Retrieval layer
- Prompt construction layer
- Generation layer

---

## 📂 Project Structure

local-rag/
│
├── app.py
├── rag/
│   ├── ingest.py
│   ├── retriever.py
│   └── chain.py
│
├── data/           # Add your PDFs here (not tracked in Git)
├── vectorstore/    # Auto-generated vector DB (not tracked)
├── requirements.txt
└── README.md

---

## 📄 Adding Documents

This repository does not include sample PDFs.

To add your own documents:

1. Create a folder named `data/`
2. Add one or more PDF files inside:
data/
resume.pdf
architecture.pdf
policy.pdf
3. Run ingestion:
python rag/ingest.py
4. Launch the app:

---

## ⚙️ Installation

### 1️⃣ Install Ollama

Download and install Ollama from:

https://ollama.com

Start Ollama:
ollama serve

Pull Llama3 model:
ollama pull llama3

---

### 2️⃣ Install Python Dependencies

Create virtual environment:
python -m venv venv
source venv/bin/activate

Install requirements:
pip install -r requirements.txt

---

## 🔒 Git Hygiene

The following directories are excluded from version control:

- `data/`
- `vectorstore/`
- `venv/`
- `__pycache__/`

This ensures the repository remains lightweight and reproducible.

---

## 🧠 How It Works

1. PDFs are loaded and split into semantic chunks
2. Each chunk is embedded using MiniLM
3. Embeddings are stored in Chroma
4. User query is embedded
5. Most relevant chunks are retrieved
6. Retrieved context + question are passed to Llama3
7. Model generates a grounded answer

---

## 🛠 Technical Highlights

- Uses LangChain's modern LCEL pipeline (Runnable-based architecture)
- Uses cosine similarity for semantic retrieval
- Embeddings are 384-dimensional vectors
- Fully offline and local inference
- Supports multi-document search

---

## 🚀 Future Improvements

- 🔄 Conversational session memory
- 📑 Document-level filtering
- ⚡ Streaming responses
- 🌐 FastAPI backend + React frontend
- 🔁 Model switching abstraction
- 🐳 Dockerization
- ☁️ Optional cloud deployment

---

## 📌 Why This Project?

Most RAG projects rely on paid APIs.

This project demonstrates:

- How to build a fully local RAG pipeline
- How vector databases work internally
- How retrieval and generation layers interact
- Clean software architecture practices

---

## 📜 License

MIT License