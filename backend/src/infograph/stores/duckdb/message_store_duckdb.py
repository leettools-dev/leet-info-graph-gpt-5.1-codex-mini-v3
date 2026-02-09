from __future__ import annotations

import time
import uuid

from infograph.core.schemas import Message, MessageCreate
from infograph.stores.abstract_message_store import AbstractMessageStore
from infograph.stores.duckdb.base import DuckDBStoreBase


class MessageStoreDuckDB(DuckDBStoreBase, AbstractMessageStore):
    table_name = "messages"
    create_table_sql = """
        CREATE TABLE IF NOT EXISTS messages (
            message_id TEXT PRIMARY KEY,
            session_id TEXT NOT NULL,
            role TEXT NOT NULL,
            content TEXT NOT NULL,
            created_at BIGINT NOT NULL
        )
    """

    def create_message(self, message: MessageCreate) -> Message:
        message_id = uuid.uuid4().hex
        created_at = int(time.time())
        self.execute(
            "INSERT INTO messages (message_id, session_id, role, content, created_at) VALUES (?, ?, ?, ?, ?)",
            (message_id, message.session_id, message.role, message.content, created_at),
        )
        return Message(
            message_id=message_id,
            session_id=message.session_id,
            role=message.role,
            content=message.content,
            created_at=created_at,
        )

    def list_messages(self, session_id: str) -> list[Message]:
        cursor = self.execute("SELECT message_id, session_id, role, content, created_at FROM messages WHERE session_id = ? ORDER BY created_at ASC", (session_id,))
        return [
            Message(
                message_id=row[0],
                session_id=row[1],
                role=row[2],
                content=row[3],
                created_at=row[4],
            )
            for row in cursor.fetchall()
        ]

    def delete_messages(self, session_id: str) -> int:
        cursor = self.execute("DELETE FROM messages WHERE session_id = ?", (session_id,))
        return getattr(cursor, "rowcount", 0)
