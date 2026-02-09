from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Iterable

from infograph.core.schemas.message import Message, MessageCreate


class AbstractMessageStore(ABC):
    @abstractmethod
    def add_message(self, message_create: MessageCreate) -> Message:
        raise NotImplementedError

    @abstractmethod
    def list_messages(
        self, session_id: str, limit: int = 100, offset: int = 0
    ) -> Iterable[Message]:
        raise NotImplementedError

    @abstractmethod
    def get_message(self, message_id: str) -> Message | None:
        raise NotImplementedError
