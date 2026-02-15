from __future__ import annotations

from typing import Iterable

from infograph.core.schemas.message import Message, MessageCreate
from infograph.stores.abstract_message_store import AbstractMessageStore
from infograph.stores.duckdb.duckdb_client import DuckDBClient


class MessageStoreDuckDB(AbstractMessageStore):
    """DuckDB-backed Message store implementation."""

    _TABLE_NAME = "messages"
    _CREATE_TABLE_SQL = f"""
    CREATE TABLE IF NOT EXISTS { _TABLE_NAME } (
        message_id TEXT PRIMARY KEY,
        session_id TEXT NOT NULL,
        role TEXT NOT NULL,
        content TEXT NOT NULL,
        created_at INTEGER NOT NULL
    )
    """

    def __init__(self, client: DuckDBClient) -> None:
        self._client = client
        self._client.execute(self._CREATE_TABLE_SQL)

    def add_message(self, message_create: MessageCreate) -> Message:
        message = Message.from_create(message_create)
        self._client.execute(
            f"INSERT INTO {self._TABLE_NAME} (message_id, session_id, role, content, created_at)"
            " VALUES (?, ?, ?, ?, ?)",
            (
                message.message_id,
                message.session_id,
                message.role,
                message.content,
                message.created_at,
            ),
        )
        return message

    def list_messages(self, session_id: str, limit: int = 100, offset: int = 0) -> Iterable[Message]:
        rows = self._client.fetch_all(
            f"SELECT * FROM {self._TABLE_NAME} WHERE session_id = ? ORDER BY created_at DESC LIMIT ? OFFSET ?",
            (session_id, limit, offset),
        )
        return [self._row_to_message(row) for row in rows if row is not None]

    def get_message(self, message_id: str) -> Message | None:
        row = self._client.fetch_one(
            f"SELECT * FROM {self._TABLE_NAME} WHERE message_id = ?",
            (message_id,),
        )
        return self._row_to_message(row)

    @staticmethod
    def _row_to_message(row: dict[str, object] | None) -> Message | None:
        if row is None:
            return None
        return Message.model_validate(row)
