from __future__ import annotations

from typing import Any, Iterable

from infograph.core.schemas.user import User, UserCreate
from infograph.stores.abstract_user_store import AbstractUserStore
from infograph.stores.duckdb.duckdb_client import DuckDBClient


class UserStoreDuckDB(AbstractUserStore):
    """DuckDB-backed User store for the Infograph assistant."""

    _TABLE_NAME = "users"
    _CREATE_TABLE_SQL = f"""
    CREATE TABLE IF NOT EXISTS { _TABLE_NAME } (
        user_id TEXT PRIMARY KEY,
        email TEXT NOT NULL UNIQUE,
        name TEXT NOT NULL,
        google_id TEXT NOT NULL,
        created_at INTEGER NOT NULL,
        updated_at INTEGER NOT NULL
    )
    """

    def __init__(self, client: DuckDBClient) -> None:
        self._client = client
        self._client.execute(self._CREATE_TABLE_SQL)

    def create_user(self, user_create: UserCreate) -> User:
        user = User.from_create(user_create)
        self._client.execute(
            f"INSERT INTO {self._TABLE_NAME} (user_id, email, name, google_id, created_at, updated_at)"
            " VALUES (?, ?, ?, ?, ?, ?)",
            (
                user.user_id,
                user.email,
                user.name,
                user.google_id,
                user.created_at,
                user.updated_at,
            ),
        )
        return user

    def get_user_by_email(self, email: str) -> User | None:
        row = self._client.fetch_one(
            f"SELECT * FROM {self._TABLE_NAME} WHERE email = ?",
            (email,),
        )
        return self._row_to_user(row)

    def get_user(self, user_id: str) -> User | None:
        row = self._client.fetch_one(
            f"SELECT * FROM {self._TABLE_NAME} WHERE user_id = ?",
            (user_id,),
        )
        return self._row_to_user(row)

    def list_users(self, limit: int = 100, offset: int = 0) -> Iterable[User]:
        rows = self._client.fetch_all(
            f"SELECT * FROM {self._TABLE_NAME} ORDER BY created_at DESC LIMIT ? OFFSET ?",
            (limit, offset),
        )
        return [self._row_to_user(row) for row in rows]

    @staticmethod
    def _row_to_user(row: dict[str, Any] | None) -> User | None:
        if row is None:
            return None
        return User.model_validate(row)
