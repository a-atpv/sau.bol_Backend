
from typing import Any

from pydantic import BaseSettings
from pymongo import MongoClient


class Config(BaseSettings):
    CORS_ORIGINS: list[str] = ["*"]
    CORS_HEADERS: list[str] = ["*"]
    CORS_METHODS: list[str] = ["GET", "POST", "PUT", "PATCH", "DELETE", "OPTIONS"]

    MONGOHOST: str = "localhost"
    MONGOPORT: str = "27017"
    MONGOUSER: str = "root"
    MONGOPASSWORD: str = "password"
    MONGODATABASE: str = "fastapi"
    MONGO_URL: str = ""


# environmental variables
env = Config()

# FastAPI configurations
fastapi_config: dict[str, Any] = {
    "title": "API",
}

mongo_url = (
    f"mongodb://{env.MONGOUSER}:{env.MONGOPASSWORD}@{env.MONGOHOST}:{env.MONGOPORT}/"
)
if env.MONGO_URL:
    mongo_url = env.MONGO_URL

# MongoDB connection
client = MongoClient(mongo_url)

# MongoDB database
database = client[env.MONGODATABASE]

# def read_questions_to_dict(filename):
#     data = []
#     with open(filename, "r") as file:
#         reader = csv.DictReader(file)
#         for row in reader:
#             question = row["question"]
#             meaning = row["meaning"]

#             data.append(
#                 {
#                     "question": question,
#                     "meaning": meaning
#                 }
#             )
#     return data


# def upload_data(data):
#     database["shortTest"].insert_many(data)


# filename = "questionData.csv"
# data = read_questions_to_dict(filename)
# upload_data(data)
