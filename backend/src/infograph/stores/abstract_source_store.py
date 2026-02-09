from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Iterable

from infograph.core.schemas.source import Source, SourceCreate


class AbstractSourceStore(ABC):
    @abstractmethod
    def add_source(self, source_create: SourceCreate) -> Source:
        raise NotImplementedError

    @abstractmethod
    def list_sources(self, session_id: str) -> Iterable[Source]:
        raise NotImplementedError

    @abstractmethod
    def get_source(self, source_id: str) -> Source | None:
        raise NotImplementedError
