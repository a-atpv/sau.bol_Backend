from pymongo import MongoClient

mongo_url = (
    f"mongodb://{'root'}:{'password'}@{'localhost'}:{'27017'}/"
)

client = MongoClient(mongo_url)

# MongoDB database
database = client['fastapi']


def delete_data():
    database["doctors"].delete_many({})


delete_data()
