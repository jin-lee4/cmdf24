import pymongo
import sys

from DbFunctions import DbFunctions

class UserDB(DbFunctions):
    """
    Class to handle interactions with User database
    """
    def __init__(self):
        super().__init__()
        self.userCollection = self.db["users"]
        self.mentorProfiles = self.db["mentorProfiles"]
        self.menteeProfiles = self.db["menteeProfiles"]

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

    def get_name(self, id):
        """
        Function that returns name of user with given id
        :param id: ObjectId
        :return: String
        """
        user = self.userCollection.find_one({"_id": id})
        return user["name"].split()[0]

    def get_email(self, id):
        """
        function that returns email of user with given id
        :param id: ObjectId of user
        :return: String
        """
        user = self.userCollection.find_one({"_id": id})
        return user["email"]

    def update_self_identification(self, user_id, self_id):
        """
        updates self_identification field, adds if doesn't exist
        :param user_id: ObjectId of user
        :param self_id: self identification (List)
        :return: None
        """
        try:
            self.userCollection.find_one_and_update({"_id": user_id}, {"$set": {"self-idenfication": self_id}})
        except pymongo.errors.OperationFailure:
            print(
                "An authentication error was received. Are you sure your database user is authorized to perform write operations?")
            sys.exit(1)
    def add_field(self, user_id, name, field):
        """
        adds field to user, updates it if already exists
        :param user_id: ObjectId of user
        :param name: name of field
        :param field: field value
        """
        try:
            self.userCollection.find_one_and_update({"_id": user_id}, {"$set": {name: field}})
        except pymongo.errors.OperationFailure:
            print(
                "An authentication error was received. Are you sure your database user is authorized to perform write operations?")
            sys.exit(1)

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
                "specialties": preferences
            })
        except pymongo.errors.OperationFailure:
            print(
                "An authentication error was received. Are you sure your database user is authorized to perform write operations?")
            sys.exit(1)

    def make_mentee_profile(self, user_id, preferences):
        """
        Function that creates mentee profile for given user id
        :param user_id: ObjectId
        :param preferences: preferences
        :return: None
        """
        try:
            self.menteeProfiles.insert_one({
                "_id": user_id,
                "interests": preferences
            })
        except pymongo.errors.OperationFailure:
            print(
                "An authentication error was received. Are you sure your database user is authorized to perform write operations?")
            sys.exit(1)

    def get_profiles(self, type):
        """
        Function that gets all mentor/mentee profiles
        :param type: String; either "mentor" or "mentee".
        """
        if type == "mentor":
            col = self.mentorProfiles
        else:
            col = self.menteeProfiles
        try:
            profiles = col.distinct("_id", {})
            return profiles
        except pymongo.errors.OperationFailure:
            print(
                "An authentication error was received. Are you sure your database user is authorized to perform write operations?")
            sys.exit(1)

    def pair_up(self, user_id, id, type):
        if type == "mentor":
            str = "mentors"
        else:
            str = "mentees"
        try:
            self.userCollection.find_one_and_update({"_id": user_id}, {"$addToSet": {str: id}})
        except pymongo.errors.OperationFailure:
            print(
                "An authentication error was received. Are you sure your database user is authorized to perform write operations?")
            sys.exit(1)

    def get_all_pairs(self, user_id, pair_type):
        if pair_type == "mentor":
            str = "mentors"
        else:
            str = "mentees"
        try:
            user = self.userCollection.find_one({"_id": user_id})
            return user[str]
        except pymongo.errors.OperationFailure:
            print("Error.")
            sys.exit(1)

    def get_preferences(self, id, type):
        """
        gets preferences of user
        :param id: ObjectId of user
        :param type: String; either "mentor" or "mentee"
        :return: preferences
        """
        if type == "mentor":
            col = self.mentorProfiles
            preferences_field = "specialties"
        else:
            col = self.menteeProfiles
            preferences_field = "interests"
        try:
            user = col.find_one({"_id": id})
            return user.get(preferences_field)
        except pymongo.errors.OperationFailure:
            print(
                "An authentication error was received. Are you sure your database user is authorized to perform write operations?")
            sys.exit(1)



if __name__ == "__main__":
    user = UserDB()
    user.add_user("user1", "<EMAIL>", "passwrod")
    print(user.get_profiles("mentor"))
