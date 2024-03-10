from datetime import datetime

import pymongo
import sys

from bson import ObjectId

from DbFunctions import DbFunctions
from user_db_functions import UserDB
class ChatDB(DbFunctions):
    """
    Class to handle interactions with messages database
    """
    def __init__(self):
        super().__init__()
        self.messages = self.db["messages"]
        self.chats = self.db["chats"]

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

    def make_new_chat(self, mentor, mentee):
        """
        creates a new chat between mentor and mentee
        :param mentor: ObjectId of mentor
        :param mentee: ObjetcId of mentee
        :return: None
        """
        self.chats.insert_one(
            {
                "mentor": mentor,
                "mentee": mentee
            }
        )

    def add_summary(self, mentor, mentee, summary):
        """
        adds summary to chat between given mentor and mentee
        :param mentor: mentor ObjectId
        :param mentee: mentee ObjectId
        :param summary: String
        :return: None
        """
        try:
            self.chats.find_one_and_update({"mentor": mentor, "mentee": mentee}, {"$addToSet": {"summaries": summary}})
        except pymongo.errors.OperationFailure:
            print(
                "An authentication error was received. Are you sure your database user is authorized to perform write operations?")
            sys.exit(1)

    def get_messages(self, message_from, message_to, from_date=None, to_date=datetime.now()):
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
            })
            if allMsg:
                for message in allMsg:
                    append = True
                    if from_date is not None:
                        if not (from_date <= message["message_dateTime"] <= to_date):
                            append = False
                    if append:
                        messages.append(message["message"])
            return messages
        except pymongo.errors.OperationFailure:
            print(
                "An authentication error was received. Are you sure your database user is authorized to perform write operations?")
            sys.exit(1)

    def get_summaries(self, mentee):
        """
        returns all summaries for a given user
        :param mentee: ObjectId of user
        :return: List[String]
        """
        try:
            summaries = self.chats.find({"mentee": mentee}, {"summaries": 1, "_id": 0})
            return summaries
        except pymongo.errors.OperationFailure:
            print(
                "An authentication error was received. Are you sure your database user is authorized to perform write operations?")
            sys.exit(1)



# Testing
if __name__ == "__main__":
    chatDb = ChatDb()
    userDb = UserDB()
    user = userDb.get_id("admin")
    chatDb.add_message("hellow world 2", user, user)
    print(chatDb.get_messages(user, user))
    print(chatDb.get_messages(user, user, datetime(2024, 2, 1)))
