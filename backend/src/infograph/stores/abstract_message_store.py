from __future__ import annotations

from abc import ABC, abstractmethod

from infograph.core.schemas import Message, MessageCreate


class AbstractMessageStore(ABC):
    @abstractmethod
    def create_message(self, message: MessageCreate) -> Message:
        ...

    @abstractmethod
    def list_messages(self, session_id: str) -> list[Message]:
        ...

    @abstractmethod
    def delete_messages(self, session_id: str) -> int:
        ...
