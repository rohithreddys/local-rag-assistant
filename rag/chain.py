from langchain_community.chat_models import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from rag.retriever import get_retriever


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

    # Format retrieved docs into a single string
    def format_docs(docs):
        return "\n\n".join(doc.page_content for doc in docs)

    # Build LCEL pipeline
    chain = (
        {
            "context": retriever | format_docs,
            "question": RunnablePassthrough()
        }
        | prompt
        | llm
        | StrOutputParser()
    )

    return chain