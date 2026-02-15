from __future__ import annotations

from typing import Iterable

from infograph.core.schemas.research_session import ResearchSession, ResearchSessionCreate
from infograph.stores.abstract_session_store import AbstractSessionStore
from infograph.stores.duckdb.duckdb_client import DuckDBClient


class SessionStoreDuckDB(AbstractSessionStore):
    """DuckDB-backed ResearchSession store."""

    _TABLE_NAME = "sessions"
    _CREATE_TABLE_SQL = f"""
    CREATE TABLE IF NOT EXISTS { _TABLE_NAME } (
        session_id TEXT PRIMARY KEY,
        user_id TEXT NOT NULL,
        prompt TEXT NOT NULL,
        status TEXT NOT NULL,
        created_at INTEGER NOT NULL,
        updated_at INTEGER NOT NULL
    )
    """

    def __init__(self, client: DuckDBClient) -> None:
        self._client = client
        self._client.execute(self._CREATE_TABLE_SQL)

    def create_session(self, user_id: str, session_create: ResearchSessionCreate) -> ResearchSession:
        session = ResearchSession.from_create(session_create, user_id)
        self._client.execute(
            f"INSERT INTO {self._TABLE_NAME} (session_id, user_id, prompt, status, created_at, updated_at)"
            " VALUES (?, ?, ?, ?, ?, ?)",
            (
                session.session_id,
                session.user_id,
                session.prompt,
                session.status,
                session.created_at,
                session.updated_at,
            ),
        )
        return session

    def get_session(self, session_id: str) -> ResearchSession | None:
        row = self._client.fetch_one(
            f"SELECT * FROM {self._TABLE_NAME} WHERE session_id = ?",
            (session_id,),
        )
        return self._row_to_session(row)

    def list_sessions(self, user_id: str, limit: int = 100, offset: int = 0) -> Iterable[ResearchSession]:
        rows = self._client.fetch_all(
            f"SELECT * FROM {self._TABLE_NAME} WHERE user_id = ? ORDER BY created_at DESC LIMIT ? OFFSET ?",
            (user_id, limit, offset),
        )
        return [self._row_to_session(row) for row in rows if row is not None]

    def delete_session(self, session_id: str) -> bool:
        self._client.execute(
            f"DELETE FROM {self._TABLE_NAME} WHERE session_id = ?",
            (session_id,),
        )
        return self.get_session(session_id) is None

    @staticmethod
    def _row_to_session(row: dict[str, object] | None) -> ResearchSession | None:
        if row is None:
            return None
        return ResearchSession.model_validate(row)
