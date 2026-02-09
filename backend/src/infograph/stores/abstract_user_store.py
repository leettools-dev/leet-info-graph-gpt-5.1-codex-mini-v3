from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Iterable

from infograph.core.schemas import User, UserCreate


class AbstractUserStore(ABC):
    """Defines the interface for storing and retrieving user data."""

    @abstractmethod
    def create_user(self, user_create: UserCreate) -> User:
        """Persist a new user."""

    @abstractmethod
    def get_user_by_id(self, user_id: str) -> User | None:
        """Return a user by their UUID."""

    @abstractmethod
    def get_user_by_google_id(self, google_id: str) -> User | None:
        """Return a user by their Google identifier."""

    @abstractmethod
    def list_users(self, limit: int = 100, offset: int = 0) -> list[User]:
        """List users for administrative purposes."""

    @abstractmethod
    def update_user(
        self,
        user_id: str,
        *,
        name: str | None = None,
        email: str | None = None,
    ) -> User | None:
        """Update mutable fields for an existing user."""

    @abstractmethod
    def delete_user(self, user_id: str) -> bool:
        """Remove a user by their identifier."""
