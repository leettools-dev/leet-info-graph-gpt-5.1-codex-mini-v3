from __future__ import annotations

from datetime import datetime
from typing import Literal
from uuid import uuid4

from pydantic import BaseModel


STATUS_PENDING = "pending"
STATUS_SEARCHING = "searching"
STATUS_GENERATING = "generating"
STATUS_COMPLETED = "completed"
STATUS_FAILED = "failed"
STATUS_CHOICES = (
    STATUS_PENDING,
    STATUS_SEARCHING,
    STATUS_GENERATING,
    STATUS_COMPLETED,
    STATUS_FAILED,
)


class ResearchSessionCreate(BaseModel):
    prompt: str


class ResearchSession(BaseModel):
    session_id: str
    user_id: str
    prompt: str
    status: Literal[
        STATUS_PENDING,
        STATUS_SEARCHING,
        STATUS_GENERATING,
        STATUS_COMPLETED,
        STATUS_FAILED,
    ]
    created_at: int
    updated_at: int

    @classmethod
    def from_create(
        cls,
        payload: ResearchSessionCreate,
        user_id: str,
        status: Literal[
            STATUS_PENDING,
            STATUS_SEARCHING,
            STATUS_GENERATING,
            STATUS_COMPLETED,
            STATUS_FAILED,
        ] = STATUS_PENDING,
    ) -> "ResearchSession":
        timestamp = int(datetime.utcnow().timestamp())
        return cls(
            session_id=str(uuid4()),
            user_id=user_id,
            prompt=payload.prompt,
            status=status,
            created_at=timestamp,
            updated_at=timestamp,
        )
