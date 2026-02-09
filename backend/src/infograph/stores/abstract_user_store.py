from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Iterable

from infograph.core.schemas.user import User, UserCreate


class AbstractUserStore(ABC):
    @abstractmethod
    def create_user(self, user_create: UserCreate) -> User:
        raise NotImplementedError

    @abstractmethod
    def get_user_by_email(self, email: str) -> User | None:
        raise NotImplementedError

    @abstractmethod
    def get_user(self, user_id: str) -> User | None:
        raise NotImplementedError

    @abstractmethod
    def list_users(self, limit: int = 100, offset: int = 0) -> Iterable[User]:
        raise NotImplementedError
