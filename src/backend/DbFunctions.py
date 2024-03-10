from datetime import datetime

import pymongo
import os
from dotenv import load_dotenv
from pymongo.server_api import ServerApi

load_dotenv(".env")

class DbFunctions:
    '''
    Class to connect to MongoDB
    '''
    def __init__(self):
        # self.client = pymongo.MongoClient(os.environ.get('DB_CONNECTION_STRING'))
        self.client = pymongo.MongoClient("mongodb+srv://dbUser:cvQ57t6OcNLmparC@cmdf24.kdwggsi.mongodb.net/?retryWrites=true&w=majority&appName=cmdf24")
        self.db = self.client.orbitDb

    def getDb(self):
        return self.db
