from fastapi import Depends
from app.utils import AppModel
# from typing import List
from app.auth.adapters.jwt_service import JWTData
from ..service import Service, get_service
from . import router
from app.auth.router.dependencies import parse_jwt_user_data
# from pymongo.results import DeleteResult


# class DeletUserRequest(AppModel):
#     user_id: str


# class DeleteHabitResponse(AppModel):
#     status: DeleteResult


@router.post("/user-delete")
def delete_user(
    # data: DeletUserRequest,
    jwt_data: JWTData = Depends(parse_jwt_user_data),
    svc: Service = Depends(get_service),
):
    print("Router Deleting...")
    svc.repository.delete_user(
        jwt_data.user_id
    )
