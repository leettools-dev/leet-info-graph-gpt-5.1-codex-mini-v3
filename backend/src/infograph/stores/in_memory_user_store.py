from __future__ import annotations

from typing import Iterable

from infograph.core.schemas.user import User, UserCreate
from infograph.stores.abstract_user_store import AbstractUserStore


class InMemoryUserStore(AbstractUserStore):
    """Lightweight user store that keeps users in memory."""

    def __init__(self) -> None:
        self._users_by_id: dict[str, User] = {}
        self._email_index: dict[str, str] = {}

    def create_user(self, user_create: UserCreate) -> User:
        user = User.from_create(user_create)
        self._users_by_id[user.user_id] = user
        self._email_index[user.email.lower()] = user.user_id
        return user

    def get_user_by_email(self, email: str) -> User | None:
        user_id = self._email_index.get(email.lower())
        if not user_id:
            return None
        return self._users_by_id.get(user_id)

    def get_user(self, user_id: str) -> User | None:
        return self._users_by_id.get(user_id)

    def list_users(self, limit: int = 100, offset: int = 0) -> Iterable[User]:
        users = list(self._users_by_id.values())
        return users[offset : offset + limit]
