from __future__ import annotations

from abc import ABC, abstractmethod

from infograph.core.schemas import Source, SourceCreate


class AbstractSourceStore(ABC):
    @abstractmethod
    def create_source(self, source: SourceCreate) -> Source:
        ...

    @abstractmethod
    def list_sources(self, session_id: str) -> list[Source]:
        ...

    @abstractmethod
    def delete_sources_for_session(self, session_id: str) -> int:
        ...
