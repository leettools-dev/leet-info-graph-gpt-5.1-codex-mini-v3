from __future__ import annotations

from datetime import datetime
from uuid import uuid4

from pydantic import BaseModel


class UserCreate(BaseModel):
    email: str
    name: str
    google_id: str


class User(BaseModel):
    user_id: str
    email: str
    name: str
    google_id: str
    created_at: int
    updated_at: int

    @classmethod
    def from_create(cls, payload: UserCreate) -> "User":
        timestamp = int(datetime.utcnow().timestamp())
        return cls(
            user_id=str(uuid4()),
            email=payload.email,
            name=payload.name,
            google_id=payload.google_id,
            created_at=timestamp,
            updated_at=timestamp,
        )
