from pymongo import MongoClient

class DB:

    def __init__(self):

        self.client = MongoClient('mongodb://root:password@ds145639.mlab.com:45639/readly')
        self.db = self.client.readly
