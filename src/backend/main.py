from datetime import datetime

from flask import Flask, request, redirect, jsonify, session
from flask_cors import CORS
from user_db_functions import UserDB
from my_cohere import MyCohere
from chat_db_functions import ChatDb
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'bad_secret_key'
app = CORS(app)
# socketio = SocketIO(app)
user_db = UserDB()
chat_db = ChatDb()
cohere_ai = MyCohere()

@app.route("/api/login", methods=['GET', 'POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    if user_db.login(email, password):
        return jsonify({"message": "Login successful."})
    else:
        return jsonify({"message": "Invalid login."}), 401

@app.route("/api/signup", methods=['GET', 'POST'])
def signup():
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    password = data.get('password')
    if not user_db.is_user(email):
        user_db.add_user(name, email, password)
        return jsonify({"message": "Signup successful."})
    else:
        return jsonify({"message": "Invalid login."}), 401

@app.route("/api/get-mentors", methods=['GET', 'POST'])



@app.route("/api/match-mentors", methods=['GET'])
def match_mentors():
    data = request.get_json()
    user_id = user_db.get_id(data.get('email'))
    matches = cohere_ai.user_matching(user_id, "mentee")
    return jsonify({"matches": matches})

@app.route("/api/match-mentees", methods=['GET'])
def match_mentees():
    data = request.get_json()
    user_id = user_db.get_id(data.get('email'))
    matches = cohere_ai.user_matching(user_id, "mentor")
    return jsonify({"matches": matches})

@app.route("/api/get-messages", methods=['GET'])
def get_messages():
    data = request.get_json()
    from_id = user_db.get_id(data.get('email'))
    to_id = user_db.get_id(data.get('to email'))
    messages = chat_db.get_messages(from_id, to_id, datetime.now() - 7)
    return jsonify({"messages": messages})

@app.route("/api/sent-message", methods=['POST'])
def send_message():
    data = request.get_json()
    user_id = user_db.get_id((data.get('email')))
    to_id = user_db.get_id(data.get('to email'))
    chat_db.add_message(data.get('message'), user_id, to_id)
    return jsonify({"message": "Saved successfully."})

@app.route("/api/save-summary", methods=['POST'])
def save_summary():
    data = request.get_json()
    user_id = user_db.get_id(data.get('email'))
