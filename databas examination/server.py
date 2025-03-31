from flask import Flask, render_template, request, redirect, session
from flask_socketio import SocketIO, send, emit
import mysql.connector


app = Flask(__name__) 
app.secret_key = 'banan'
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
    if "username" not in session:
        return redirect("/signup")

    return render_template('index.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    error_message = None
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        # Kontrollera om användarnamnet redan finns
        cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
        existing_user = cursor.fetchone()

        if existing_user:
            error_message = "Användarnamnet är redan upptaget. Vänligen välj ett annat."
        else:
            # Skapa ett nytt konto
            session["username"] = username
            cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
            conn.commit()
            return redirect("/")

    return render_template('signup.html', error_message=error_message)

@app.route('/signin', methods=['GET', 'POST'])
def signin():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        cursor.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, password))
        user = cursor.fetchone()

        if user:
            session["username"] = username
            return redirect("/")
        else:
            return "Fel användarnamn eller lösenord", 401

    return render_template('signin.html')

@socketio.on('message')
def handle_message(msg):
    user = session["username"]

    # spara meddelandet i databasen
    cursor.execute("INSERT INTO messages (user, message) VALUES (%s, %s)", (user, msg))
    conn.commit()

    # skicka meddelandet till alla anslutna klienter
    emit('message', {'user': user, 'msg': msg}, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000)
