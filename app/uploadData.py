# import csv


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
#         return data


# def upload_data(self, data):

#     self.database["shortTest"].insert_many(data)


# filename = "questionData.csv"
# data = read_questions_to_dict(filename)
# upload_data(data=data)
