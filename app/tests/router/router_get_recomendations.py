from fastapi import Depends
from app.utils import AppModel
from typing import List
from app.auth.adapters.jwt_service import JWTData
from ..service import Service, get_service
from . import router
from app.auth.router.dependencies import parse_jwt_user_data


class RecommendationRequest(AppModel):
    symptoms: List[str]


class RecommendationResponse(AppModel):
    recommendations: dict


@router.post("/recommendations", response_model=RecommendationResponse)
def get_recommendations(
    data: RecommendationRequest,
    jwt_data: JWTData = Depends(parse_jwt_user_data),
    svc: Service = Depends(get_service),
) -> RecommendationResponse:
    print(data.symptoms)
    recommendations = svc.ai_svc.get_recommendations(data.symptoms)
    return RecommendationResponse(recommendations=recommendations)
