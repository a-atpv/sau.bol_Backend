# from datetime import datetime
from typing import Dict, Any, List

from bson.objectid import ObjectId
from pymongo.database import Database
# from ...auth.repository.repository import AuthRepository


class HabitRepository:
    def __init__(self, database: Database):
        self.database = database

    def create_habit(self, user_id: str, habit: str):
        return self.database["habits"].insert_one({
            "description": habit,
            "achieved_dates": [],  # 2023-09-30
            "user_id": user_id,
        })

    def add_new_date_to_habit(self, habit_id: str, date: str):
        self.database["habits"].update_one(
            filter={"_id": ObjectId(habit_id)},
            update={
                "$push": {"achieved_dates": date}
            }
        )

    def get_habits(self, user_id: str) -> List[Dict[str, Any]]:
        habits = self.database["habits"].find(
            filter={"user_id": user_id}
        )
        return list(habits)

    def delete_habit(self, habit_id: str):
        return self.database["habits"].delete_one(
            filter={"_id": ObjectId(habit_id)}
        )
