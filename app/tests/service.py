from pydantic import BaseSettings

from app.config import database

from .adapters.jwt_service import JwtService
from .repository.repository import TestRepository
from .adapters.ai_service import AiService


class AuthConfig(BaseSettings):
    JWT_ALG: str = "HS256"
    JWT_SECRET: str = "dgjisDsddfvfdgDsegsDFgdf#2#wdsf*&344533sdff+sdfSd"
    JWT_EXP: int = 10_800


config = AuthConfig()


class Service:
    def __init__(
        self,
        repository: TestRepository,
        jwt_svc: JwtService,
    ):
        self.repository = repository
        self.jwt_svc = jwt_svc
        self.ai_svc = AiService()


def get_service():
    repository = TestRepository(database)
    jwt_svc = JwtService(config.JWT_ALG, config.JWT_SECRET, config.JWT_EXP)
    svc = Service(repository, jwt_svc)
    return svc
