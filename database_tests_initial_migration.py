import csv

from pymongo import MongoClient

mongo_url = (
    "mongodb+srv://a_atpv:5dPxFUsXYwMvMiH@cluster0.kplqazt.mongodb.net/?retryWrites=true&w=majority"
)

client = MongoClient(mongo_url)

# MongoDB database
database = client['fastapi']


def read_questions_to_dict(filename):
    data = []
    with open(filename, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            question = row["question"]
            meaning = row["meaning"]

            data.append(
                {
                    "question": question,
                    "meaning": meaning
                }
            )
    return data


def upload_data(data):
    database["shortTest"].insert_many(data)


filename = "questionData.csv"
data = read_questions_to_dict(filename)
upload_data(data)
