from __future__ import annotations

from pydantic import BaseModel, Field

from infograph.core.schemas.user import User


class GoogleAuthRequest(BaseModel):
    credential: str = Field(..., description="Google credential obtained from client-side authentication")


class AuthResponse(BaseModel):
    token: str
    user: User
