import pymongo
import sys
from DbFunctions import DbFunctions

class UserDB(DbFunctions):
    """
    Class to handle interactions with User database
    """
    def __init__(self):
        super().__init__()
        self.userDb = self.client.userInfo
        self.userCollection = self.userDb["users"]
        self.mentorProfiles = self.userDb["mentorProfiles"]
        self.menteeProfiles = self.userDb["menteeProfiles"]

    def add_user(self, name, email, password):
        """
        Function that adds user to database
        :param name: name of the user to be added
        :param email: email of user to be added
        :param password: password of user to be added
        """
        try:
            result = self.userCollection.insert_one({
                "name": name,
                "email": email,
                "password": password
            })
        except pymongo.errors.OperationFailure:
            print(
                "An authentication error was received. Are you sure your database user is authorized to perform write operations?")
            sys.exit(1)

    def login(self, email, password):
        """
        Function that checks if given email and password matches existing user login
        :param email: email of user
        :param password: password of user
        :return: True if in database, False otherwise
        """
        all_users = self.userCollection.find()
        if all_users:
            for user in all_users:
                if user["email"] == email and user["password"] == password:
                    return True
        return False

    def is_user(self, email):
        """
        Function that checks if user with email exists
        :param email: email of user
        :return: True if in database, False otherwise
        """
        user = self.userCollection.find_one({"email": email})
        if user is not None:
            return True
        else:
            return False

    def get_id(self, email):
        """
        Function that returns ObjectId of user with given email
        :param email: email of user
        :return: ObjectId
        """
        user = self.userCollection.find_one({"email": email})
        return user["_id"]

    def make_mentor_profile(self, user_id, preferences):
        """
        Function that creates mentor profile for given used id
        :param user_id: ObjectId
        :param preferences: List of preferences
        :return: None
        """
        try:
            self.mentorProfiles.insert_one({
                "_id": user_id,
                "preferences": preferences
            })
        except pymongo.errors.OperationFailure:
            print(
                "An authentication error was received. Are you sure your database user is authorized to perform write operations?")
            sys.exit(1)

    def make_mentee_profile(self, user_id, preferences):
        """
        Function that creates mentee profile for given user id
        :param user_id: ObjectId
        :param preferences: List of preferences
        :return: None
        """
        try:
            self.menteeProfiles.insert_one({
                "_id": user_id,
                "preferences": preferences
            })
        except pymongo.errors.OperationFailure:
            print(
                "An authentication error was received. Are you sure your database user is authorized to perform write operations?")
            sys.exit(1)


if __name__ == "__main__":
    user = UserDB()
    id = user.get_id("admin")
    user.make_mentor_profile(id, ["<NAME>", "<NAME>", "<NAME>", "<NAME>"])
