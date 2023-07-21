from fastapi import Depends
from app.utils import AppModel
from app.auth.adapters.jwt_service import JWTData
from ..service import Service, get_service
from . import router
from app.auth.router.dependencies import parse_jwt_user_data


class CreateHabitRequest(AppModel):
    habit: str


class CreateHabitResponse(AppModel):
    status: int


@router.post("/create", response_model=CreateHabitResponse)
def create_habit(
    data: CreateHabitRequest,
    jwt_data: JWTData = Depends(parse_jwt_user_data),
    svc: Service = Depends(get_service),
) -> CreateHabitResponse:
    svc.repository.create_habit(
        jwt_data.user_id,
        data.habit
    )
    return CreateHabitResponse(status=200)
