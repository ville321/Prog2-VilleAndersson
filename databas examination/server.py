from flask import Flask, render_template, request, redirect, session
from flask_socketio import SocketIO, send, emit
import mysql.connector

app = Flask(__name__) 
socketio = SocketIO(app)

conn = mysql.connector.connect( # koppla till mysql databasen
  host="localhost",
  user="root",  
  password="",  
  database="chat_forum" 
)
cursor = conn.cursor()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        session["username"] = username
        cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
        conn.commit()

        return redirect("/")
    return render_template('signup.html')

@socketio.on('message')
def handle_message(msg):
    user = session["username"]

    # spara meddelandet i databasen
    cursor.execute("INSERT INTO messages (user, message) VALUES (%s, %s)", (user, msg))
    conn.commit()

    # skicka meddelandet till alla anslutna klienter
    emit('message', {'user': user, 'msg': msg}, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, debug=True)
