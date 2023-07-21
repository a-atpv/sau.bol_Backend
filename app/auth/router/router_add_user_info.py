from fastapi import Depends

from ..router.dependencies import parse_jwt_user_data
from ..adapters.jwt_service import JWTData
# from fastapi.security import OAuth2PasswordRequestForm

from app.utils import AppModel

from ..service import Service, get_service
from ..utils.security import check_password
from . import router
from .errors import InvalidCredentialsException


class AddUserInfoRequest(AppModel):
    name: str
    age: str
    height: str
    weight: str
    BMI: str 

    def makeDict(self):
        dict = {
            "name": self.name,
            "age": self.age,
            "height": self.height,
            "weight": self.weight,
            "BMI": self.BMI        
        }
        return dict


class AddUserInfoResponse(AppModel):
    status: str


@router.post("/users/info", response_model=AddUserInfoResponse)
def add_user_info(
    input: AddUserInfoRequest,
    jwt_data: JWTData = Depends(parse_jwt_user_data),
    svc: Service = Depends(get_service),
) -> AddUserInfoResponse:
    svc.repository.add_user_info(
        jwt_data.user_id,
        input.makeDict()
    )

    return AddUserInfoResponse(
        status="OK"
    )
