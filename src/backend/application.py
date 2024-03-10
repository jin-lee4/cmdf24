from flask import Flask
from flask_socketio import SocketIO

from DbFunctions import DbFunctions


def create_app():
    app = Flask(__name__)
    socketio = SocketIO(app)

    db = DbFunctions().getDb()
    mongo = db(app.config["MONGO_HOSTNAME"], app.config["MONGO_PORT"])
    app.db = mongo[app.config["MONGO_APP_DATABASE"]]


    return app
