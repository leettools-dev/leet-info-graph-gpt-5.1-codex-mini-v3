from __future__ import annotations

from datetime import datetime
from typing import Literal
from uuid import uuid4

from pydantic import BaseModel


class MessageCreate(BaseModel):
    session_id: str
    role: Literal["user", "assistant", "system"]
    content: str


class Message(BaseModel):
    message_id: str
    session_id: str
    role: Literal["user", "assistant", "system"]
    content: str
    created_at: int

    @classmethod
    def from_create(cls, payload: MessageCreate) -> "Message":
        return cls(
            message_id=str(uuid4()),
            session_id=payload.session_id,
            role=payload.role,
            content=payload.content,
            created_at=int(datetime.utcnow().timestamp()),
        )
