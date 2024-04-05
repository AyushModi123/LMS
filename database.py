from pymongo import MongoClient
from pymongo.collection import Collection
import os

url = os.getenv("MONGO_DB_URL")
client = MongoClient(url)


def get_db():        
    db = client.get_database("cosmocloud_assignment")
    collection = db.get_collection("students")
    return collection
