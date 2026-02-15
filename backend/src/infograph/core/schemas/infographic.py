from __future__ import annotations

from datetime import datetime
from typing import Any
from uuid import uuid4

from pydantic import BaseModel


class InfographicCreate(BaseModel):
    session_id: str
    image_path: str
    template_type: str
    layout_data: dict[str, Any]


class Infographic(BaseModel):
    infographic_id: str
    session_id: str
    image_path: str
    template_type: str
    layout_data: dict[str, Any]
    created_at: int

    @classmethod
    def from_create(cls, payload: InfographicCreate) -> "Infographic":
        timestamp = int(datetime.utcnow().timestamp())
        return cls(
            infographic_id=str(uuid4()),
            session_id=payload.session_id,
            image_path=payload.image_path,
            template_type=payload.template_type,
            layout_data=payload.layout_data,
            created_at=timestamp,
        )
