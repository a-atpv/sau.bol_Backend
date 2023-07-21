from typing import Dict, Any, List

from pymongo.database import Database


class DoctorRepository:
    def __init__(self, database: Database):
        self.database = database

    # def create_habit(self, user_id: str, habit: str):
    #     return self.database["habits"].insert_one({
    #         "description": habit,
    #         "achieved_dates": [],  # 2023-09-30
    #         "user_id": user_id,
    #     })

    # def add_new_date_to_habit(self, habit_id: str, date: str):
    #     self.database["habits"].update_one(
    #         filter={"_id": ObjectId(habit_id)},
    #         update={
    #             "$push": {"achieved_dates": date}
    #         }
    #     )

    def get_doctors(self) -> List[Dict[str, Any]]:
        doctors = self.database["doctors"].find({})
        return list(doctors)

    # def delete_habit(self, habit_id: str):
    #     return self.database["habits"].delete_one(
    #         filter={"_id": ObjectId(habit_id)}
    #     )
