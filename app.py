import gradio as gr
from rag.chain import get_qa_chain

qa_chain = get_qa_chain()

def ask_question(question):
    return qa_chain(question)

interface = gr.Interface(
    fn=ask_question,
    inputs="text",
    outputs="text",
    title="Local Multi-Document RAG Assistant"
)

interface.launch()