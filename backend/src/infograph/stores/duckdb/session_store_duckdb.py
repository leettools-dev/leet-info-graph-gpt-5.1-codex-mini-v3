from __future__ import annotations

import time
import uuid
from typing import Iterable

from infograph.core.schemas import ResearchSession, ResearchSessionCreate
from infograph.stores.abstract_session_store import AbstractResearchSessionStore
from infograph.stores.duckdb.base import DuckDBStoreBase


class ResearchSessionStoreDuckDB(DuckDBStoreBase, AbstractResearchSessionStore):
    table_name = "research_sessions"
    create_table_sql = """
        CREATE TABLE IF NOT EXISTS research_sessions (
            session_id TEXT PRIMARY KEY,
            user_id TEXT NOT NULL,
            prompt TEXT NOT NULL,
            status TEXT NOT NULL,
            created_at BIGINT NOT NULL,
            updated_at BIGINT NOT NULL
        )
    """

    def create_session(self, user_id: str, session_data: ResearchSessionCreate) -> ResearchSession:
        now = int(time.time())
        session_id = uuid.uuid4().hex
        status = "pending"
        self.execute(
            "INSERT INTO research_sessions (session_id, user_id, prompt, status, created_at, updated_at) VALUES (?, ?, ?, ?, ?, ?)",
            (session_id, user_id, session_data.prompt, status, now, now),
        )
        return ResearchSession(
            session_id=session_id,
            user_id=user_id,
            prompt=session_data.prompt,
            status=status,
            created_at=now,
            updated_at=now,
        )

    def get_session(self, session_id: str) -> ResearchSession | None:
        cursor = self.execute(
            "SELECT session_id, user_id, prompt, status, created_at, updated_at FROM research_sessions WHERE session_id = ?",
            (session_id,),
        )
        row = cursor.fetchone()
        if not row:
            return None
        return ResearchSession(
            session_id=row[0],
            user_id=row[1],
            prompt=row[2],
            status=row[3],
            created_at=row[4],
            updated_at=row[5],
        )

    def list_sessions(self, user_id: str, limit: int = 20, offset: int = 0) -> list[ResearchSession]:
        cursor = self.execute(
            "SELECT session_id, user_id, prompt, status, created_at, updated_at FROM research_sessions WHERE user_id = ? ORDER BY created_at DESC LIMIT ? OFFSET ?",
            (user_id, limit, offset),
        )
        return [
            ResearchSession(
                session_id=row[0],
                user_id=row[1],
                prompt=row[2],
                status=row[3],
                created_at=row[4],
                updated_at=row[5],
            )
            for row in cursor.fetchall()
        ]

    def delete_session(self, session_id: str) -> bool:
        cursor = self.execute("DELETE FROM research_sessions WHERE session_id = ?", (session_id,))
        return getattr(cursor, "rowcount", 0) != 0
