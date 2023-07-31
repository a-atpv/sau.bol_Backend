import openai
from typing import List
from dotenv import load_dotenv
import os


class AiService:
    def __init__(self):
        load_dotenv()
        OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
        openai.api_key = OPENAI_API_KEY


def get_recommendations(self, symptoms: List[str]) -> str:
    symptoms_text = ", ".join(symptoms)
    user_message = ""
    if len(symptoms) == 0:
        user_message = (
            "У меня нет проблем со здоровьем дай 3 рекомендации по"
            "анализам и укажи причины почему мне нужны эти анализы ,  и 3 "
            "привычки, которым надо придерживаться каждый день, "
            "привычки объяснять не надо, каждая рекомендация по "
            "привычке  должна содержать 8 слов максимум. если говоришь "
            "принимать какие-то добавки или пищу, указывай объем, "
            "привычка должна быть строго измеряемая, "
            "ответ должен содержать 180 слов максимум, привычки должны "
            "быть конкретными и измеряемыми, "
            "ответ должен придти в формате json, вот формат: "
            '{"intro": "перечисли проблемы человека", '
            '"analisys": ["анализ1", "анализ2"], '
            '"habits": ["привычка1", "привычка2"], '
            '"conclusion": "заключительное предложение", '
            '"resourse": "научную статью на которую ссылаешься, указывай ссылку"}')
    else:
        user_message = (
            f"У меня возможно есть такие проблемы: {symptoms_text} "
            "дай 3 рекомендации по анализам и укажи причины почему мне нужны эти анализы, "
            "и 3 привычки, которым надо придерживаться каждый день, "
            "привычки объяснять не надо, каждая рекомендация по привычке должна содержать 8 слов максимум, "
            "если говоришь принимать какие-то добавки или пищу, указывай объем, "
            "привычка должна быть строго измеряемая, "
            "ответ должен содержать 180 слов максимум"
            "ответ должен придти в формате json, вот формат: "
            '{"intro": "перечисли проблемы человека", '
            '"analisys": ["анализ1", "анализ2"], '
            '"habits": ["привычка1", "привычка2"], '
            '"conclusion": "заключительное предложение", '
            '"resourse": "научную статью на которую ссылаешься, указывай ссылку"}'
        )

    response = openai.Completion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Ты доктор, помогающий поднять качество жизни"},
            {"role": "user", "content": user_message},
        ],
        temperature=0.7,
    )

    return response['choices'][0]['message']['content'].strip()