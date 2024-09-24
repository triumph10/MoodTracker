# import gradio as gr
# import os
# import gradio as gr
# import google.generativeai as genai
# from dotenv import load_dotenv, find_dotenv



# load_dotenv(find_dotenv())

# genai.configure(api_key=os.getenv('GEMINI_API_KEY'))

# model = genai.GenerativeModel()

# def handle_user_query(msg, chatbot):
#     print(msg, chatbot)
#     chatbot += [[msg, None]]
#     return '', chatbot

# def generate_chatbot(chatbot: list[list[str, str]]) -> list[list[str, str]]:
#     formatted_chatbot = []
#     if len(chatbot) == 0:
#         return formatted_chatbot
#     for ch in chatbot:
#         formatted_chatbot.append(
#             {
#                 "role": "user",
#                 "parts": [ch[0]]
#             }
#         )
#         formatted_chatbot.append(
#             {
#                 "role": "model",
#                 "parts": [ch[1]]
#             }
#         )
#     return formatted_chatbot

# def handle_gemini_response(chatbot):
#     query = chatbot[-1][0]
#     formatted_chatbot = generate_chatbot(chatbot[:-1])
#     chat = model.start_chat(history=formatted_chatbot)
#     response = chat.send_message(query)
#     chatbot[-1][1] = response.text
#     return chatbot

# with gr.Blocks() as demo:
#     chatbot = gr.Chatbot(
#         label='Chat with Gemini',
#         bubble_full_width=False,
#     )
#     msg = gr.Textbox()
#     clear = gr.ClearButton([msg, chatbot])
#     msg.submit(
#        handle_user_query,
#        [msg, chatbot],
#        [msg, chatbot] 
#     ).then(
#         handle_gemini_response,
#         [chatbot],
#         [chatbot]
#     )

# if __name__ == "__main__":
#     demo.queue()
#     demo.launch()

# import gradio as gr
# import os
# import google.generativeai as genai
# from dotenv import load_dotenv, find_dotenv

# def launch_gradio():
#     # Load environment variables from .env file
#     load_dotenv(find_dotenv())

#     # Configure Google Generative AI with API key
#     genai.configure(api_key=os.getenv('GEMINI_API_KEY'))
#     model = genai.GenerativeModel()

#     def handle_user_query(msg, chatbot):
#         print(f"User: {msg}")
#         chatbot += [[msg, None]]
#         return '', chatbot

#     def generate_chatbot(chatbot: list[list[str, str]]) -> list[list[str, str]]:
#         formatted_chatbot = []
#         if len(chatbot) == 0:
#             return formatted_chatbot
#         for ch in chatbot:
#             formatted_chatbot.append({
#                 "role": "user",
#                 "parts": [ch[0]]
#             })
#             formatted_chatbot.append({
#                 "role": "model",
#                 "parts": [ch[1]]
#             })
#         return formatted_chatbot

#     def handle_gemini_response(chatbot):
#         query = chatbot[-1][0]
#         formatted_chatbot = generate_chatbot(chatbot[:-1])
#         chat = model.start_chat(history=formatted_chatbot)
#         response = chat.send_message(query)
#         chatbot[-1][1] = response.text
#         print(f"Bot: {response.text}")
#         return chatbot

#     with gr.Blocks() as demo:
#         chatbot_ui = gr.Chatbot(
#             label='Chat with Gemini',
#             bubble_full_width=False,
#         )
#         msg = gr.Textbox(
#             placeholder="Type your message here...",
#             label="Your Message"
#         )
#         clear = gr.ClearButton([msg, chatbot_ui])
#         msg.submit(
#            handle_user_query,
#            [msg, chatbot_ui],
#            [msg, chatbot_ui] 
#         ).then(
#             handle_gemini_response,
#             [chatbot_ui],
#             [chatbot_ui]
#         )

#     demo.queue()
#     demo.launch(
#         server_name="0.0.0.0",
#         server_port=7860,
#         share=False,
#         inbrowser=False
#     )

# import gradio as gr
# import os
# import google.generativeai as genai
# from dotenv import load_dotenv, find_dotenv

# # Load environment variables from .env file
# load_dotenv(find_dotenv())

# # Configure Google Generative AI with API key
# api_key = os.getenv('GEMINI_API_KEY')
# print("GEMINI_API_KEY:", api_key)  # Debugging line
# genai.configure(api_key=api_key)

# model = genai.GenerativeModel()

# def handle_user_query(msg, chatbot):
#     print(msg, chatbot)
#     chatbot += [[msg, None]]
#     return '', chatbot

# def generate_chatbot(chatbot: list[list[str, str]]) -> list[list[str, str]]:
#     formatted_chatbot = []
#     if len(chatbot) == 0:
#         return formatted_chatbot
#     for ch in chatbot:
#         formatted_chatbot.append(
#             {
#                 "role": "user",
#                 "parts": [ch[0]]
#             }
#         )
#         formatted_chatbot.append(
#             {
#                 "role": "model",
#                 "parts": [ch[1]]
#             }
#         )
#     return formatted_chatbot

# def handle_gemini_response(chatbot):
#     try:
#         query = chatbot[-1][0]
#         formatted_chatbot = generate_chatbot(chatbot[:-1])
#         chat = model.start_chat(history=formatted_chatbot)
#         response = chat.send_message(query)
#         chatbot[-1][1] = response.text
#         print(f"Bot: {response.text}")
#     except Exception as e:
#         print(f"Error in handle_gemini_response: {e}")  # Log the error
#         chatbot[-1][1] = "Sorry, there was an error processing your request."
#     return chatbot

# # Set up the Gradio interface
# with gr.Blocks() as demo:
#     chatbot = gr.Chatbot(
#         label='Chat with Gemini',
#         bubble_full_width=False,
#     )
#     msg = gr.Textbox()
#     clear = gr.ClearButton([msg, chatbot])
#     msg.submit(
#         handle_user_query,
#         [msg, chatbot],
#         [msg, chatbot]
#     ).then(
#         handle_gemini_response,
#         [chatbot],
#         [chatbot]
#     )

# if __name__ == "__main__":
#     demo.queue()
#     demo.launch()

import gradio as gr
import os
import google.generativeai as genai
from dotenv import load_dotenv, find_dotenv

# Load environment variables from .env file
load_dotenv(find_dotenv())

# Configure Google Generative AI with API key
api_key = os.getenv('GEMINI_API_KEY')
print("GEMINI_API_KEY:", api_key)  # Debugging line
genai.configure(api_key=api_key)

# Create the model instance
model = genai.GenerativeModel()

def handle_user_query(msg, chatbot):
    print(msg, chatbot)
    chatbot += [[msg, None]]
    return '', chatbot

def generate_chatbot(chatbot: list[list[str, str]]) -> list[list[str, str]]:
    formatted_chatbot = []
    if len(chatbot) == 0:
        return formatted_chatbot
    for ch in chatbot:
        formatted_chatbot.append(
            {
                "role": "user",
                "parts": [ch[0]]
            }
        )
        formatted_chatbot.append(
            {
                "role": "model",
                "parts": [ch[1]]
            }
        )
    return formatted_chatbot

def handle_gemini_response(chatbot):
    try:
        query = chatbot[-1][0]
        formatted_chatbot = generate_chatbot(chatbot[:-1])
        chat = model.start_chat(history=formatted_chatbot)
        response = chat.send_message(query)
        chatbot[-1][1] = response.text
        print(f"Bot: {response.text}")
    except Exception as e:
        print(f"Error in handle_gemini_response: {e}")  # Log the error
        chatbot[-1][1] = "Sorry, there was an error processing your request."
    return chatbot

def launch_gradio():
    # Set up the Gradio interface
    with gr.Blocks() as demo:
        chatbot = gr.Chatbot(
            label='Chat with Gemini',
            bubble_full_width=False,
        )
        msg = gr.Textbox()
        clear = gr.ClearButton([msg, chatbot])
        msg.submit(
            handle_user_query,
            [msg, chatbot],
            [msg, chatbot]
        ).then(
            handle_gemini_response,
            [chatbot],
            [chatbot]
        )

    demo.queue()
    demo.launch()  # You can pass parameters here as needed

if __name__ == "__main__":
    launch_gradio()  # Call the function when running this script

