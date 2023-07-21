from typing import Dict, Any
from pymongo.database import Database


class TestRepository:
    def __init__(self, database: Database):
        self.database = database

    def get_all_short_tests(self) -> Dict[str, Any]:
        tests = self.database["shortTest"].find({})
        response = {
            "questions": list(tests)
        }
        return response
