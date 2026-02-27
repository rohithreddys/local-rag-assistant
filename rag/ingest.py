import os
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings


def ingest_documents():

    data_path = "data"
    all_documents = []

    print("Loading PDFs...")

    for file in os.listdir(data_path):
        if file.endswith(".pdf"):
            file_path = os.path.join(data_path, file)
            print(f"Loading {file}...")

            loader = PyPDFLoader(file_path)
            documents = loader.load()

            # Add file name to metadata
            for doc in documents:
                doc.metadata["source_file"] = file

            all_documents.extend(documents)

    print(f"Total pages loaded: {len(all_documents)}")

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=150
    )

    chunks = splitter.split_documents(all_documents)

    print(f"Total chunks created: {len(chunks)}")

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    vectorstore = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory="vectorstore"
    )

    vectorstore.persist()

    print("Multi-document vectorstore created successfully!")


if __name__ == "__main__":
    ingest_documents()