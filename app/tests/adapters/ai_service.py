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
        user_message = self._generate_user_message(symptoms)

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Ты доктор, помогающий поднять качество жизни"},
                {"role": "user", "content": user_message},
            ],
            temperature=0.5,
        )

        return response['choices'][0]['message']['content'].strip()

    def _generate_user_message(self, symptoms: List[str]) -> str:
        if len(symptoms) == 0:
            user_message = (
                "У меня нет проблем со здоровьем. "
                "Дай 3 рекомендации по анализам и укажи причины, почему мне нужны эти анализы, "
                "и 3 привычки, для улучшения качества жизни. "
                "Если привычка это принимать какие-то добавки или пищу, указывай объем. "
                "Привычка должна быть строго измеряемой. "
                "Привычки должны быть конкретными и измеряемыми. "
                "Третья привычка должна быть рекомендацией по приему конкретных витаминов или минералов "
                "в соответствии с моим заболеванием. "
                "Ответ должен придти в формате JSON. Вот формат: "
                '{"intro": "перечисли мои возможные проблемы", '
                '"analysis": ["анализ1", "анализ2"], '
                '"explanation": "объяснение почему именно эти анализы", '
                '"habits": ["привычка1", "привычка2"], '
                '"conclusion": "заключительное предложение"}'
            )
        else:
            symptoms_text = ", ".join(symptoms)
            user_message = (
                f"У меня возможно есть такие проблемы: {symptoms_text}. "
                "Дай 3 рекомендации по анализам и укажи причины, почему мне нужны эти анализы, "
                "и 3 привычки, для улучшения качества жизни. "
                "Если привычка это принимать какие-то добавки или пищу, указывай объем. "
                "Привычка должна быть строго измеряемой. "
                "Привычки должны быть конкретными и измеряемыми. "
                "Третья привычка должна быть рекомендацией по приему конкретных витаминов или минералов "
                "в соответствии с моим заболеванием. "
                "Ответ должен придти в формате JSON. Вот формат: "
                '{"intro": "перечисли мои возможные проблемы", '
                '"analysis": ["анализ1", "анализ2"], '
                '"explanation": "объяснение почему именно эти анализы", '
                '"habits": ["привычка1", "привычка2", "привычка3 (прием витаминов/минералов)"], '
                '"conclusion": "заключительное предложение"}'
            )

        return user_message
