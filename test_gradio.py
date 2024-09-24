import gradio as gr

def chatbot_fn(msg):
    return f"Chatbot response to: {msg}"

# Create the Gradio interface
interface = gr.Interface(fn=chatbot_fn, inputs="text", outputs="text")

# Launch the Gradio interface
interface.launch()
