from pymongo import MongoClient

mongo_url = (
    "mongodb+srv://a_atpv:5dPxFUsXYwMvMiH@cluster0.kplqazt.mongodb.net/?retryWrites=true&w=majority"
)

client = MongoClient(mongo_url)

# MongoDB database
database = client['fastapi']


def delete_data():
    database["doctors"].delete_many({})


delete_data()
