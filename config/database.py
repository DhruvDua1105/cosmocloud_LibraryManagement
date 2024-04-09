from pymongo import MongoClient

client = MongoClient("mongodb+srv://dhruvduansut2024:iCYbnrkmNICcKnrD@mongofastapi.eoiyrvd.mongodb.net/")

db = client.student_db
collection_name = db["students"]