from datetime import datetime

from bson import ObjectId
from flask import Flask, request, jsonify
from flask_cors import CORS
from user_db_functions import UserDB
from my_cohere import MyCohere
from chat_db_functions import ChatDB

app = Flask(__name__)
CORS(app)

user_db = UserDB()
chat_db = ChatDB()
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

@app.route("/api/make-mentor", methods=['POST'])
def make_mentor():
    data = request.get_json()
    id = user_db.get_id(data.get('email'))
    specialties = data.get('specialties')
    user_db.make_mentor_profile(id, specialties)
    return jsonify({"message": "Mentor added."})

@app.route("/api/make-mentee", methods=['POST'])
def make_mentee():
    data = request.get_json()
    id = user_db.get_id(data.get('email'))
    interests = data.get('interests')
    user_db.make_mentor_profile(id, interests)
    return jsonify({"message": "Mentee added."})

@app.route("/api/get-mentors", methods=['GET'])
def get_mentors():
    data = request.get_json()
    id = user_db.get_id(data.get('email'))
    mentors = user_db.get_all_pairs(id, "mentors")
    return jsonify({"mentors": filter_user_list(mentors)})


@app.route("/api/get-mentees", methods=['GET'])
def get_mentees():
    data = request.get_json()
    id = user_db.get_id(data.get('email'))
    mentees = user_db.get_all_pairs(id, "mentees")
    return jsonify({"mentors": filter_user_list(mentees)})

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
    list = filter_user_list(matches)
    return jsonify({"matches": list})

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
    to_id = user_db.get_id(data.get('to email'))
    chat_db.add_summary(user_id, to_id, data.get('summary'))

def filter_user_list(user_list):
    """
    Converts list of ObjectIds into list of emails
    :param user_list: List of ObjectIds/String
    :return: List[String]
    """
    new_user_list = []
    for user in user_list:
        if isinstance(user, str):
            new_user_list.append(user_db.get_email(ObjectId(user)))
        else:
            new_user_list.append(user_db.get_email(user))
    return new_user_list


if __name__ == "__main__":
    app.run(debug=True, port=8080)
