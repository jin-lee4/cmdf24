from flask import Flask, request, redirect, jsonify, session
from flask_cors import CORS
from user_db_functions import UserDB
from my_cohere import MyCohere
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'bad_secret_key'
app = CORS(app)
# socketio = SocketIO(app)
user_db = UserDB()
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
