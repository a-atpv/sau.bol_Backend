from fastapi import Depends, HTTPException, status, Response

from app.utils import AppModel

from ..service import Service, get_service
from . import router


class PasswordResetTokenRequest(AppModel):
    email: str


@router.post("/password-reset-token")
def password_reset_token(
    input: PasswordResetTokenRequest,
    svc: Service = Depends(get_service),
) -> dict[str, str]:
    reset_token = svc.repository.reset_password(email=input.email)
    if reset_token is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Cannot reset password for this email. Please try again",
        )
    if not svc.repository.send_reset_token_email(email=input.email, reset_token=reset_token):
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error has happened when sending password reset email",
        )
    return Response(status_code=status.HTTP_200_OK)
