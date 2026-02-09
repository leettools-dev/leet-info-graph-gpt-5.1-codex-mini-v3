from __future__ import annotations

from abc import ABC, abstractmethod

from infograph.core.schemas import Infographic, InfographicCreate


class AbstractInfographicStore(ABC):
    @abstractmethod
    def create_infographic(self, infographic_data: InfographicCreate) -> Infographic:
        ...

    @abstractmethod
    def get_infographic(self, session_id: str) -> Infographic | None:
        ...

    @abstractmethod
    def delete_infographic(self, infographic_id: str) -> bool:
        ...
