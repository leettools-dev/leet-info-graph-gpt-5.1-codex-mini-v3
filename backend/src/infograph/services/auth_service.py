from __future__ import annotations

from datetime import datetime, timedelta
from typing import Any

from google.auth.transport.requests import Request
from google.oauth2 import id_token
from jose import jwt

from infograph.core.schemas.auth import GoogleAuthRequest, AuthResponse
from infograph.core.schemas.user import UserCreate, User
from infograph.stores.abstract_user_store import AbstractUserStore


class AuthService:
    def __init__(self, user_store: AbstractUserStore, client_id: str, jwt_secret: str) -> None:
        self._user_store = user_store
        self._client_id = client_id
        self._jwt_secret = jwt_secret
        self._algorithm = "HS256"

    def verify_google_token(self, credential: str) -> UserCreate:
        request = Request()
        id_info = id_token.verify_oauth2_token(credential, request, self._client_id)
        if id_info.get("iss") not in ("accounts.google.com", "https://accounts.google.com"):
            raise ValueError("Invalid token issuer")

        return UserCreate(
            email=id_info["email"],
            name=id_info.get("name", ""),
            google_id=id_info["sub"],
        )

    def authenticate(self, payload: GoogleAuthRequest) -> AuthResponse:
        user_create = self.verify_google_token(payload.credential)
        user = self._user_store.get_user_by_email(user_create.email)
        if not user:
            user = self._user_store.create_user(user_create)

        token = self._create_jwt(user)
        return AuthResponse(token=token, user=user)

    def get_user_from_token(self, token: str) -> User:
        claims = jwt.decode(token, self._jwt_secret, algorithms=[self._algorithm])
        user_id = claims.get("sub")
        if not user_id:
            raise ValueError("Token missing user identifier")

        user = self._user_store.get_user(user_id)
        if not user:
            raise ValueError("User not found for token")

        return user

    def _create_jwt(self, user: User) -> str:
        now = datetime.utcnow()
        expiry = now + timedelta(hours=24)
        payload: dict[str, Any] = {
            "sub": user.user_id,
            "email": user.email,
            "name": user.name,
            "exp": int(expiry.timestamp()),
        }
        return jwt.encode(payload, self._jwt_secret, algorithm=self._algorithm)
