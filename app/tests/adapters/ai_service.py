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
            user_message = "У меня нет проблем со здоровьем \
            дай 3 рекомендации по анализам и укажи причины почему мне нужны эти анализы , \
            и 3 привычки, для улучшения качества жини, \
            привычки объяснять не надо, \
            каждая рекомендация дожна содержать 8 слов максимум \
            если говоришь принимать какие то добавки или пищу, указывай объем \
            привычка должна быть строго измеряемая \
            примеры нужных пунктов: \
            - 10.000 шагов в день \
            - принимать 5 капель витамина д \
            - пить 1,5 литра воды \
            - есть 100 грамм клетчатки в день \
            ответ должен содержать 180 слов максимум, привычки должны быть конкретными и измеряемыми"
        else:
            user_message = f"У меня возможно есть такие проблемы: {symptoms_text} \
            кратко перечисли мои проблемы и дай 3 рекомендации по анализам и укажи причины почему мне нужны эти анализы , \
            и 3 конкретные привычки для предотврощения уходшения этих проблем {symptoms_text}\
            привычки объяснять не надо, \
            каждая рекомендация по привычке должна содержать 8 слов максимум \
            если говоришь принимать какие то добавки или пищу, указывай объем \
            привычка должна быть строго измеряемая \
            ответ должен содержать 180 слов максимум"

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Ты доктор, помогающий \
                 поднять качество жизни"},
                {"role": "user", "content": user_message},
            ],
            temperature=0.7,
        )

        return response['choices'][0]['message']['content'].strip()

