# backend.py
import os
import google.generativeai as genai
from dotenv import load_dotenv, find_dotenv

def initialize_model():
    load_dotenv(find_dotenv())
    genai.configure(api_key=os.getenv('GEMINI_API_KEY'))
    return genai.GenerativeModel()

def handle_user_query(msg, chatbot):
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

def handle_gemini_response(chatbot, model):
    query = chatbot[-1][0]
    formatted_chatbot = generate_chatbot(chatbot[:-1])
    chat = model.start_chat(history=formatted_chatbot)
    response = chat.send_message(query)
    chatbot[-1][1] = response.text
    return chatbot
