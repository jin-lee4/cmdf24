from flask import Blueprint, render_template, request, redirect, jsonify
from flask import current_app as app
from user_db_functions import UserDB

blueprint = Blueprint("orbit", __name__)


@blueprint.route("/", methods=['GET'])
def get():
    redirect("/login")

@blueprint.route("/login", methods=['GET', 'POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    user_db = UserDB()
    if user_db.login(email, password):
        return jsonify({"message": "Login successful."})
    else:
        return jsonify({"message": "Invalid login."}), 401


