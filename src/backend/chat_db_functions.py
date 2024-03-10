from datetime import datetime

import pymongo
import sys

from bson import ObjectId

from DbFunctions import DbFunctions
from user_db_functions import UserDB
class ChatDb(DbFunctions):
    """
    Class to handle interactions with messages database
    """
    def __init__(self):
        super().__init__()
        self.chatDb = self.client.messagesDb
        self.messages = self.chatDb["messages"]

    def add_message(self, message, msg_from, msg_to):
        """
        adds a message to the database
        :param message: text message content
        :param msg_from: ObjectId of user who sent msg
        :param msg_to: ObjectId of user who received msg
        :return: None
        """
        try:
            self.messages.insert_one(
                {
                    "message": message,
                    "message_from": msg_from,
                    "message_to": msg_to,
                    "message_dateTime": datetime.now()
                }
            )
        except pymongo.errors.OperationFailure:
            print(
                "An authentication error was received. Are you sure your database user is authorized to perform write operations?")
            sys.exit(1)

    def get_messages(self, message_from, message_to):
        """
        gets all chat between two users
        :param message_from: ObjectId of user who sent msg
        :param message_to: ObjectId of user who received msg
        :return: List[String]
        """
        messages = []
        try:
            allMsg = self.messages.find({
                "message_from": message_from,
                "message_to": message_to
            }).sort("message_dateTime")
            if allMsg:
                for message in allMsg:
                    messages.append(message["message"])
            return messages
        except pymongo.errors.OperationFailure:
            print(
                "An authentication error was received. Are you sure your database user is authorized to perform write operations?")
            sys.exit(1)

# Testing
if __name__ == "__main__":
    chatDb = ChatDb()
    userDb = UserDB()
    user = userDb.get_id("admin")
    print(chatDb.get_messages(user, user))