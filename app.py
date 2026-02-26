import gradio as gr
from rag.chain import get_qa_chain

qa_chain = get_qa_chain()

def ask_question(question):
    answer = qa_chain.invoke(question)
    return answer

interface = gr.Interface(
    fn=ask_question,
    inputs="text",
    outputs="text",
    title="Local RAG Assistant (100% Free)"
)

interface.launch()