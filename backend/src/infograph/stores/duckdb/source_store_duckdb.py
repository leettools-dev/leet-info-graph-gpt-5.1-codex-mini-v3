from __future__ import annotations

import time
import uuid

from infograph.core.schemas import Source, SourceCreate
from infograph.stores.abstract_source_store import AbstractSourceStore
from infograph.stores.duckdb.base import DuckDBStoreBase


class SourceStoreDuckDB(DuckDBStoreBase, AbstractSourceStore):
    table_name = "sources"
    create_table_sql = """
        CREATE TABLE IF NOT EXISTS sources (
            source_id TEXT PRIMARY KEY,
            session_id TEXT NOT NULL,
            title TEXT NOT NULL,
            url TEXT NOT NULL,
            snippet TEXT NOT NULL,
            confidence REAL NOT NULL,
            fetched_at BIGINT NOT NULL
        )
    """

    def create_source(self, source: SourceCreate) -> Source:
        source_id = uuid.uuid4().hex
        fetched_at = int(time.time())
        self.execute(
            "INSERT INTO sources (source_id, session_id, title, url, snippet, confidence, fetched_at) VALUES (?, ?, ?, ?, ?, ?, ?)",
            (source_id, source.session_id, source.title, source.url, source.snippet, source.confidence, fetched_at),
        )
        return Source(
            source_id=source_id,
            session_id=source.session_id,
            title=source.title,
            url=source.url,
            snippet=source.snippet,
            confidence=source.confidence,
            fetched_at=fetched_at,
        )

    def list_sources(self, session_id: str) -> list[Source]:
        cursor = self.execute(
            "SELECT source_id, session_id, title, url, snippet, confidence, fetched_at FROM sources WHERE session_id = ? ORDER BY fetched_at DESC",
            (session_id,),
        )
        return [
            Source(
                source_id=row[0],
                session_id=row[1],
                title=row[2],
                url=row[3],
                snippet=row[4],
                confidence=row[5],
                fetched_at=row[6],
            )
            for row in cursor.fetchall()
        ]

    def delete_sources_for_session(self, session_id: str) -> int:
        cursor = self.execute("DELETE FROM sources WHERE session_id = ?", (session_id,))
        return getattr(cursor, "rowcount", 0)
