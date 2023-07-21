from pymongo import MongoClient

mongo_url = (
    f"mongodb://{'root'}:{'password'}@{'localhost'}:{'27017'}/"
)

client = MongoClient(mongo_url)

# MongoDB database
database = client['fastapi']


def create_doctor_data(image: str, name: str, price: str, info: str):
    data = []

    data.append(
        {
            "image": image,
            "name": name,
            "price": price,
            "info": info
        }
    )
    return data


def upload_data(data):
    database["doctors"].insert_many(data)


data = create_doctor_data(
    image="https://img.freepik.com/free-photo/beautiful-young-female-doctor-looking-at-camera-in-the-office_1301-7807.jpg?w=2000",
    name="Сыздыкова Мадина Муратовна",
    price="15000",
    info="Доктор Мадина Муратовна Сыздыкова - выдающийся педиатр с более чем 20-летним \
        опытом работы. Она является обладательницей степени доктора философии (PhD) и \
        специализируется на повышении качества жизни детей. Ее преданность и забота\
        о маленьких пациентах делают ее истинным даром для общества. Сыздыкова \
        Мадина Муратовна применяет самые передовые методы и инновационные подходы \
        своей работе, чтобы обеспечить максимальное благополучие детей и их семей. \
        Благодаря ее умению устанавливать доверительные отношения и непревзойденному \
        медицинскому опыту, она пользуется уважением как среди пациентов, так и среди \
        коллег. Доктор Сыздыкова - надежный проводник в мире здоровья и счастья для \
        детей."
)

upload_data(data)
