# ui.py
import gradio as gr
from backend import initialize_model, handle_user_query, handle_gemini_response

model = initialize_model()

def handle_submission(msg, chatbot):
    chatbot = handle_user_query(msg, chatbot)
    return handle_gemini_response(chatbot, model)

def setup_ui():
    with gr.Blocks() as demo:
        chatbot = gr.Chatbot(
            label='Chat with Gemini',
            bubble_full_width=False,
        )
        msg = gr.Textbox()
        clear = gr.ClearButton([msg, chatbot])
        msg.submit(
            handle_submission,
            [msg, chatbot],
            [msg, chatbot] 
        )
    return demo

if __name__ == "__main__":
    demo = setup_ui()
    demo.queue()
    demo.launch()
