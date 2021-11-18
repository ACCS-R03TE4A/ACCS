from pymongo import MongoClient
from flaskr.config import DATABASE_NAME

client = MongoClient()
db = client[DATABASE_NAME]