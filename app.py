# from flask import Flask, render_template
# import gradio as gr

# app = Flask(__name__)

# # Define the Gradio interface
# def gradio_interface():
#     def chatbot_fn(msg):
#         return f"Chatbot response to: {msg}"
    
#     return gr.Interface(fn=chatbot_fn, inputs="text", outputs="text")

# # Route for Main Page (Page 1)
# @app.route('/')
# @app.route('/mainpage')
# def mainpage():
#     return render_template('mainpage.html')  # mainpage.html should be in templates/ folder

# # Route for Login Page (Page 2)
# @app.route('/login')
# def login():
#     return render_template('login.html')  # login.html should be in templates/ folder

# # Route for Chatbot with Gradio
# @app.route('/chatbot')
# def chatbot():
#     print("Chatbot route accessed")
#     return gradio_interface().launch(inline=True, share=False)

# # Route for Mood Tracker
# @app.route('/moodtracker')
# def moodtracker():
#     return render_template('moodtracker.html')  # moodtracker.html should be in templates/ folder


# if __name__ == '__main__':
#     app.run(port=5000, debug=True)

# from flask import Flask, render_template
# import threading
# from chatbot.gradio_ui import launch_gradio

# app = Flask(__name__)

# # Start Gradio in a separate daemon thread
# gradio_thread = threading.Thread(target=launch_gradio, daemon=True)
# gradio_thread.start()

# # Route for Main Page (Page 1)
# @app.route('/')
# @app.route('/mainpage')
# def mainpage():
#     return render_template('mainpage.html')  # Ensure mainpage.html is in templates/

# # Route for Login Page (Page 2)
# @app.route('/login')
# def login():
#     return render_template('login.html')  # Ensure login.html is in templates/

# # Route to Embed Chatbot
# @app.route('/chatbot_page')
# def chatbot_page():
#     return render_template('chatbot_page.html')  # Ensure chatbot_page.html is in templates/

# # Route for Mood Tracker
# @app.route('/moodtracker')
# def moodtracker():
#     return render_template('moodtracker.html')  # Ensure moodtracker.html is in templates/

# if __name__ == '__main__':
#     app.run(port=5000, debug=True)

from flask import Flask, render_template
from chatbot.gradio_ui import launch_gradio

app = Flask(__name__)

# Route for Main Page (Page 1)
@app.route('/')
@app.route('/mainpage')
def mainpage():
    return render_template('mainpage.html')  # mainpage.html should be in templates/ folder

@app.route('/moodtracker')
def moodtracker():
    return render_template('moodtracker.html')

# Route for Login Page (Page 2)
@app.route('/login')
def login():
    return render_template('login.html')  # login.html should be in templates/ folder

# Route for Chatbot
@app.route('/chatbot')
def chatbot():
    print("Chatbot route accessed")
    return launch_gradio()  # Launch the Gradio interface



if __name__ == '__main__':
    app.run(port=5000, debug=True)
