from __future__ import annotations

from fastapi import APIRouter, Depends, HTTPException, Security
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from jose import JWTError

from infograph.core.schemas.auth import AuthResponse, GoogleAuthRequest
from infograph.core.schemas.user import User
from infograph.services.auth_service import AuthService


bearer = HTTPBearer(auto_error=True)


def create_auth_router(auth_service: AuthService) -> APIRouter:
    router = APIRouter()


    @router.post("/auth/google", response_model=AuthResponse, status_code=200)
    async def exchange_google_token(payload: GoogleAuthRequest) -> AuthResponse:
        return auth_service.authenticate(payload)


    @router.get("/auth/me", response_model=User)
    async def get_current_user(
        token: HTTPAuthorizationCredentials = Security(bearer),
    ) -> User:
        try:
            return auth_service.get_user_from_token(token.credentials)
        except (JWTError, ValueError) as exc:
            raise HTTPException(status_code=401, detail="Invalid or expired token") from exc


    @router.post("/auth/logout")
    async def logout(
        token: HTTPAuthorizationCredentials = Security(bearer),
    ) -> dict[str, bool]:
        auth_service.get_user_from_token(token.credentials)
        return {"success": True}


    return router
