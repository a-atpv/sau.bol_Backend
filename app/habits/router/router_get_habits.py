from fastapi import Depends
from app.utils import AppModel
from typing import List
from app.auth.adapters.jwt_service import JWTData
from ..service import Service, get_service
from . import router
from app.auth.router.dependencies import parse_jwt_user_data


class GetHabitsResponse(AppModel):
    habits: List[dict]


@router.get("/me", response_model=GetHabitsResponse)
def get_habits(
    jwt_data: JWTData = Depends(parse_jwt_user_data),
    svc: Service = Depends(get_service),
) -> GetHabitsResponse:
    habits = svc.repository.get_habits(jwt_data.user_id)
    return GetHabitsResponse(habits=habits)
