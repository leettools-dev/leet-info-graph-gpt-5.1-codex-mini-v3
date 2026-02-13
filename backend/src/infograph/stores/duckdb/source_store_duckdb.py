from __future__ import annotations

from typing import Iterable

from infograph.core.schemas.source import Source, SourceCreate
from infograph.stores.abstract_source_store import AbstractSourceStore
from infograph.stores.duckdb.duckdb_client import DuckDBClient


class SourceStoreDuckDB(AbstractSourceStore):
    """DuckDB-backed Source store implementation."""

    _TABLE_NAME = "sources"
    _CREATE_TABLE_SQL = f"""
    CREATE TABLE IF NOT EXISTS { _TABLE_NAME } (
        source_id TEXT PRIMARY KEY,
        session_id TEXT NOT NULL,
        title TEXT NOT NULL,
        url TEXT NOT NULL,
        snippet TEXT NOT NULL,
        confidence REAL NOT NULL,
        fetched_at INTEGER NOT NULL
    )
    """

    def __init__(self, client: DuckDBClient) -> None:
        self._client = client
        self._client.execute(self._CREATE_TABLE_SQL)

    def add_source(self, source_create: SourceCreate) -> Source:
        source = Source.from_create(source_create)
        self._client.execute(
            f"INSERT INTO {self._TABLE_NAME} (source_id, session_id, title, url, snippet, confidence, fetched_at)"
            " VALUES (?, ?, ?, ?, ?, ?, ?)",
            (
                source.source_id,
                source.session_id,
                source.title,
                source.url,
                source.snippet,
                source.confidence,
                source.fetched_at,
            ),
        )
        return source

    def list_sources(self, session_id: str) -> Iterable[Source]:
        rows = self._client.fetch_all(
            f"SELECT * FROM {self._TABLE_NAME} WHERE session_id = ? ORDER BY fetched_at DESC",
            (session_id,),
        )
        return [self._row_to_source(row) for row in rows if row is not None]

    def get_source(self, source_id: str) -> Source | None:
        row = self._client.fetch_one(
            f"SELECT * FROM {self._TABLE_NAME} WHERE source_id = ?",
            (source_id,),
        )
        return self._row_to_source(row)

    @staticmethod
    def _row_to_source(row: dict[str, object] | None) -> Source | None:
        if row is None:
            return None
        return Source.model_validate(row)
