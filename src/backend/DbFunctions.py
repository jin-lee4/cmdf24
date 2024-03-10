from datetime import datetime

import pymongo
import os
from dotenv import load_dotenv

load_dotenv(".env")

class DbFunctions:
    '''
    Class to connect to MongoDB
    '''
    def __init__(self):
        self.client = pymongo.MongoClient(os.environ.get('DB_CONNECTION_STRING'))
