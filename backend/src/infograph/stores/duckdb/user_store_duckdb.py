from __future__ import annotations

import time
import uuid
from typing import Iterable

from infograph.core.schemas import User, UserCreate
from infograph.stores.abstract_user_store import AbstractUserStore
from infograph.stores.duckdb.base import DuckDBStoreBase


class UserStoreDuckDB(DuckDBStoreBase, AbstractUserStore):
    table_name = "users"
    create_table_sql = """
        CREATE TABLE IF NOT EXISTS users (
            user_id TEXT PRIMARY KEY,
            email TEXT NOT NULL,
            name TEXT NOT NULL,
            google_id TEXT NOT NULL UNIQUE,
            created_at BIGINT NOT NULL,
            updated_at BIGINT NOT NULL
        )
    """

    def create_user(self, user_create: UserCreate) -> User:
        now = int(time.time())
        user_id = uuid.uuid4().hex
        self.execute(
            "INSERT INTO users (user_id, email, name, google_id, created_at, updated_at) VALUES (?, ?, ?, ?, ?, ?)",
            (user_id, user_create.email, user_create.name, user_create.google_id, now, now),
        )
        return User(
            user_id=user_id,
            email=user_create.email,
            name=user_create.name,
            google_id=user_create.google_id,
            created_at=now,
            updated_at=now,
        )

    def get_user_by_id(self, user_id: str) -> User | None:
        cursor = self.execute("SELECT user_id, email, name, google_id, created_at, updated_at FROM users WHERE user_id = ?", (user_id,))
        row = cursor.fetchone()
        if not row:
            return None
        return User(
            user_id=row[0],
            email=row[1],
            name=row[2],
            google_id=row[3],
            created_at=row[4],
            updated_at=row[5],
        )

    def get_user_by_google_id(self, google_id: str) -> User | None:
        cursor = self.execute("SELECT user_id, email, name, google_id, created_at, updated_at FROM users WHERE google_id = ?", (google_id,))
        row = cursor.fetchone()
        if not row:
            return None
        return User(
            user_id=row[0],
            email=row[1],
            name=row[2],
            google_id=row[3],
            created_at=row[4],
            updated_at=row[5],
        )

    def list_users(self, limit: int = 100, offset: int = 0) -> list[User]:
        cursor = self.execute(
            "SELECT user_id, email, name, google_id, created_at, updated_at FROM users ORDER BY created_at DESC LIMIT ? OFFSET ?",
            (limit, offset),
        )
        return [
            User(
                user_id=row[0],
                email=row[1],
                name=row[2],
                google_id=row[3],
                created_at=row[4],
                updated_at=row[5],
            )
            for row in cursor.fetchall()
        ]

    def update_user(self, user_id: str, *, name: str | None = None, email: str | None = None) -> User | None:
        updates: list[str] = []
        params: list = []
        if name is not None:
            updates.append("name = ?")
            params.append(name)
        if email is not None:
            updates.append("email = ?")
            params.append(email)
        if not updates:
            return self.get_user_by_id(user_id)
        now = int(time.time())
        updates.append("updated_at = ?")
        params.append(now)
        params.append(user_id)
        query = f"UPDATE users SET {', '.join(updates)} WHERE user_id = ?"
        cursor = self.execute(query, params)
        return self.get_user_by_id(user_id) if cursor.rowcount != 0 else None

    def delete_user(self, user_id: str) -> bool:
        cursor = self.execute("DELETE FROM users WHERE user_id = ?", (user_id,))
        return getattr(cursor, "rowcount", 0) != 0
