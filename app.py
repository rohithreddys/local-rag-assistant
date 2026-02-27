import gradio as gr
from rag.chain import ConversationalRAG

rag_system = ConversationalRAG()


def ask_question(message, history):
    if history is None:
        history = []

    # Get RAG response
    answer = rag_system.ask(message)

    # Append correctly formatted messages
    history.append({"role": "user", "content": message})
    history.append({"role": "assistant", "content": answer})

    return history


def clear_chat():
    return []


with gr.Blocks() as demo:

    chatbot = gr.Chatbot()
    msg = gr.Textbox(placeholder="Ask a question about your documents...")
    clear = gr.Button("Clear")

    msg.submit(ask_question, [msg, chatbot], chatbot)
    clear.click(clear_chat, None, chatbot, queue=False)

demo.launch()