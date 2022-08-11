from pymongo import MongoClient
from config import get_settings


settings = get_settings()

client = MongoClient(settings.mongodb_url)
db = client.FastAPIMongo
student_collection = db.student_collection

def get_db():
    return student_collection