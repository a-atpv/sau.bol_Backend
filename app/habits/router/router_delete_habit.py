from fastapi import Depends
from app.utils import AppModel
# from typing import List
from app.auth.adapters.jwt_service import JWTData
from ..service import Service, get_service
from . import router
from app.auth.router.dependencies import parse_jwt_user_data
# from pymongo.results import DeleteResult


class DeleteHabitRequest(AppModel):
    habit_id: str


# class DeleteHabitResponse(AppModel):
#     status: DeleteResult


@router.post("/delete")
def delete_habit(
    data: DeleteHabitRequest,
    jwt_data: JWTData = Depends(parse_jwt_user_data),
    svc: Service = Depends(get_service),
):
    print("Router Deleting...")
    svc.repository.delete_habit(habit_id=data.habit_id)
