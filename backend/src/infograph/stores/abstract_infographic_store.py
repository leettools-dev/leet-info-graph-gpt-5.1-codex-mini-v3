from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Iterable

from infograph.core.schemas.infographic import Infographic, InfographicCreate


class AbstractInfographicStore(ABC):
    @abstractmethod
    def create_infographic(self, infographic_create: InfographicCreate) -> Infographic:
        raise NotImplementedError

    @abstractmethod
    def get_infographic(self, session_id: str) -> Infographic | None:
        raise NotImplementedError

    @abstractmethod
    def list_infographics(self, user_id: str) -> Iterable[Infographic]:
        raise NotImplementedError
