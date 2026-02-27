from langchain_community.chat_models import ChatOllama
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage, AIMessage
from rag.retriever import get_retriever


class ConversationalRAG:

    def __init__(self):
        self.retriever = get_retriever()
        self.llm = ChatOllama(model="llama3", temperature=0)
        self.chat_history = []

        self.prompt = ChatPromptTemplate.from_messages([
            ("system",
             "You are a helpful assistant. "
             "Use ONLY the provided context to answer. "
             "If the answer is not in the context, say you don't know."),
            MessagesPlaceholder(variable_name="chat_history"),
            ("human", "Context:\n{context}\n\nQuestion: {question}")
        ])

    def ask(self, question):

        docs = self.retriever.invoke(question)
        context = "\n\n".join(doc.page_content for doc in docs)

        formatted_prompt = self.prompt.format_messages(
            context=context,
            question=question,
            chat_history=self.chat_history
        )

        response = self.llm.invoke(formatted_prompt)

        # Save conversation
        self.chat_history.append(HumanMessage(content=question))
        self.chat_history.append(AIMessage(content=response.content))

        sources = list({doc.metadata.get("source_file", "Unknown") for doc in docs})

        return response.content + "\n\nSources: " + ", ".join(sources)