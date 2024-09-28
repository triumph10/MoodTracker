from flask import Flask, render_template, request, redirect, url_for, session, flash,jsonify
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re
import subprocess  # To start Streamlit programmatically
import os  # For working with file paths
from mood_track import load_resources, detect_emotion


app = Flask(__name__)

model, tokenizer = load_resources()

# Configuring Flask App
app.secret_key = 'iamironman'
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'ARYA#305#varun'
app.config['MYSQL_DB'] = 'emotion_recommendations'

mysql = MySQL(app)


# Route for Main Page (Page 1)
@app.route('/')
@app.route('/mainpage')
def mainpage():
    return render_template('mainpage.html')


@app.route('/detect_emotion', methods=['GET', 'POST'])
def moodtracker():
    if request.method == 'POST':
        data = request.get_json()
        input_text = data.get('input_text')

        # Predict the emotion
        emotion, prediction = detect_emotion(input_text, model, tokenizer)

        # Fetch recommendations from the database
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT title FROM movies WHERE emotion = %s ORDER BY RAND() LIMIT 1", (emotion,))
        movie_recommendation = cursor.fetchone()

        cursor.execute("SELECT song, artist FROM music WHERE emotion = %s ORDER BY RAND() LIMIT 1", (emotion,))
        music_recommendation = cursor.fetchone()

        cursor.execute("SELECT activity FROM exercises WHERE emotion = %s ORDER BY RAND() LIMIT 1", (emotion,))
        exercise_recommendation = cursor.fetchone()

        # Prepare the recommendations
        recommendations = {
            'emotion': emotion,
            'movies': movie_recommendation[0] if movie_recommendation else 'No movie found',
            'music': f"{music_recommendation[0]} by {music_recommendation[1]}" if music_recommendation else 'No music found',
            'exercises': exercise_recommendation[0] if exercise_recommendation else 'No exercise found'
        }

        # Return the recommendations as JSON
        return jsonify(recommendations)
    else:
        return render_template('mood_track.html')
 




# Route for Login Page (Page 2)
@app.route('/login', methods=['GET', 'POST'])
def login():
    msg = ''
    if request.method == 'POST' and 'email' in request.form and 'password' in request.form:
        email = request.form['email']
        password = request.form['password']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM accounts WHERE email = %s AND password = %s', (email, password,))
        account = cursor.fetchone()
        if account:
            session['loggedin'] = True
            session['id'] = account['id']
            session['username'] = account['email']  # Store email in session
            return redirect(url_for('mainpage'))
        else:
            msg = 'Incorrect email / password!'
    return render_template('login.html', msg=msg)




# Route for Signup Page
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    msg = ''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'email' in request.form:
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM accounts WHERE username = %s', (username,))
        account = cursor.fetchone()

        if account:
            msg = 'Account already exists!'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            msg = 'Invalid email address!'
        elif not re.match(r'[A-Za-z0-9]+', username):
            msg = 'Username must contain only characters and numbers!'
        elif not username or not password or not email:
            msg = 'Please fill out the form!'
        else:
            cursor.execute('INSERT INTO accounts (username, password, email) VALUES (%s, %s, %s)', (username, password, email))
            mysql.connection.commit()
            msg = 'You have successfully registered!'
            return redirect(url_for('login'))  # Redirect to login after successful registration
    return render_template('signup.html', msg=msg)


# Route for Chatbot
@app.route('/chatbot')
def chatbot():
    # Path to your Streamlit script
    streamlit_script = os.path.join(os.getcwd(), 'streamlit_ui.py')
    
    # Launch Streamlit as a subprocess
    subprocess.Popen(["streamlit", "run", streamlit_script])

    # Redirect to the Streamlit app once it's running
    streamlit_url = "http://localhost:8501"
    return redirect(streamlit_url)



if __name__ == '__main__':
    app.run(port=5000, debug=True)