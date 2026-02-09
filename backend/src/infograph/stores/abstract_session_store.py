from __future__ import annotations

from abc import ABC, abstractmethod

from infograph.core.schemas import Infographic, InfographicCreate, ResearchSessionCreate, ResearchSession


class AbstractResearchSessionStore(ABC):
    @abstractmethod
    def create_session(
        self,
        user_id: str,
        session_data: ResearchSessionCreate,
    ) -> ResearchSession:
        pass

    @abstractmethod
    def get_session(self, session_id: str) -> ResearchSession | None:
        pass

    @abstractmethod
    def list_sessions(self, user_id: str, limit: int, offset: int) -> list[ResearchSession]:
        pass

    @abstractmethod
    def delete_session(self, session_id: str) -> bool:
        pass
