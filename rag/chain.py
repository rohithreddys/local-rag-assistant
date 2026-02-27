from langchain_community.chat_models import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from rag.retriever import get_retriever


def format_docs(docs):
    context = "\n\n".join(doc.page_content for doc in docs)
    sources = list({doc.metadata.get("source_file", "Unknown") for doc in docs})
    return context, sources


def get_qa_chain():

    retriever = get_retriever()

    llm = ChatOllama(
        model="llama3",
        temperature=0
    )

    prompt = ChatPromptTemplate.from_template("""
    You are a helpful assistant.
    Use ONLY the provided context to answer the question.
    If the answer is not in the context, say you don't know.

    Context:
    {context}

    Question:
    {question}

    Answer:
    """)

    def rag_pipeline(question):

        docs = retriever.invoke(question)
        context, sources = format_docs(docs)

        formatted_prompt = prompt.format(
            context=context,
            question=question
        )

        response = llm.invoke(formatted_prompt)

        return response.content + "\n\nSources: " + ", ".join(sources)

    return rag_pipeline