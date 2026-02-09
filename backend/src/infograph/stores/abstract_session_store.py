from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Iterable

from infograph.core.schemas.research_session import (
    ResearchSession,
    ResearchSessionCreate,
)


class AbstractSessionStore(ABC):
    @abstractmethod
    def create_session(self, user_id: str, session_create: ResearchSessionCreate) -> ResearchSession:
        raise NotImplementedError

    @abstractmethod
    def get_session(self, session_id: str) -> ResearchSession | None:
        raise NotImplementedError

    @abstractmethod
    def list_sessions(self, user_id: str, limit: int = 100, offset: int = 0) -> Iterable[ResearchSession]:
        raise NotImplementedError

    @abstractmethod
    def delete_session(self, session_id: str) -> bool:
        raise NotImplementedError
