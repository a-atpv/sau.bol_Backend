from pydantic import BaseSettings

from app.config import database

from ..auth.adapters.jwt_service import JwtService
from .repository.repository import DoctorRepository


class AuthConfig(BaseSettings):
    JWT_ALG: str = "HS256"
    JWT_SECRET: str = "dgjisDsddfvfdgDsegsDFgdf#2#wdsf*&344533sdff+sdfSd"
    JWT_EXP: int = 10_800


config = AuthConfig()


class Service:
    def __init__(
        self,
        repository: DoctorRepository,
        jwt_svc: JwtService,
    ):
        self.repository = repository
        self.jwt_svc = jwt_svc


def get_service():
    repository = DoctorRepository(database)
    jwt_svc = JwtService(config.JWT_ALG, config.JWT_SECRET, config.JWT_EXP)
    svc = Service(repository, jwt_svc)
    return svc
