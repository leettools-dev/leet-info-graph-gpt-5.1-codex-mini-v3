from __future__ import annotations

from datetime import datetime
from uuid import uuid4

from pydantic import BaseModel


class SourceCreate(BaseModel):
    session_id: str
    title: str
    url: str
    snippet: str
    confidence: float


class Source(BaseModel):
    source_id: str
    session_id: str
    title: str
    url: str
    snippet: str
    confidence: float
    fetched_at: int

    @classmethod
    def from_create(cls, payload: SourceCreate) -> "Source":
        return cls(
            source_id=str(uuid4()),
            session_id=payload.session_id,
            title=payload.title,
            url=payload.url,
            snippet=payload.snippet,
            confidence=payload.confidence,
            fetched_at=int(datetime.utcnow().timestamp()),
        )
