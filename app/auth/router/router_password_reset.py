from fastapi import Depends, HTTPException, status, Response

from app.utils import AppModel

from ..service import Service, get_service
from . import router


class PasswordResetRequest(AppModel):
    email: str
    password: str
    token: str


@router.post("/reset-password")
def reset_password(
    input: PasswordResetRequest,
    svc: Service = Depends(get_service),
) -> dict[str, str]:
    if not svc.repository.reset_password_with_token(
            email=input.email,
            reset_token=input.token,
            new_password=input.password
    ):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Error has happened when reseting user password",
        )
    return Response(status_code=status.HTTP_200_OK)
