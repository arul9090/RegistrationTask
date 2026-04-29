import certifi
from pymongo import MongoClient
from config import Config


def create_mongo_client():
    options = {"serverSelectionTimeoutMS": 5000}
    if Config.MONGO_URI.startswith("mongodb+srv://"):
        options["tlsCAFile"] = certifi.where()
    return MongoClient(Config.MONGO_URI, **options)


client = create_mongo_client()
db = client[Config.MONGO_DB]
users = db["users"]
