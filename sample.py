import pymongo

from pymongo import MongoClient


client = MongoClient('mongodb://root:password@ds145639.mlab.com:45639/readly');
print(client)

db = client.users
print(db)
