from fastapi import Depends
from app.utils import AppModel
from typing import List
from app.auth.adapters.jwt_service import JWTData
from ..service import Service, get_service
from . import router
from app.auth.router.dependencies import parse_jwt_user_data


class GetTestResponse(AppModel):
    questions: List[dict]


@router.get("/short", response_model=GetTestResponse)
def get_short_test(
    jwt_data: JWTData = Depends(parse_jwt_user_data),
    svc: Service = Depends(get_service),
) -> GetTestResponse:
    tests = svc.repository.get_all_short_tests()
    return GetTestResponse(questions=tests.get("questions", []))
