from fastapi import Depends
from app.utils import AppModel
from typing import List
from app.auth.adapters.jwt_service import JWTData
from ..service import Service, get_service
from . import router
from app.auth.router.dependencies import parse_jwt_user_data


class GetDoctorsResponse(AppModel):
    doctors: List[dict]


@router.get("/all", response_model=GetDoctorsResponse)
def get_doctors(
    jwt_data: JWTData = Depends(parse_jwt_user_data),
    svc: Service = Depends(get_service),
) -> GetDoctorsResponse:
    doctors = svc.repository.get_doctors()
    return GetDoctorsResponse(doctors=doctors)
