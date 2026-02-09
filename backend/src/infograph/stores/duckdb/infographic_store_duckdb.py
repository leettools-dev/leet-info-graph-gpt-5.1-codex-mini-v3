from __future__ import annotations

import time
import uuid

from infograph.core.schemas import Infographic, InfographicCreate
from infograph.stores.abstract_infographic_store import AbstractInfographicStore
from infograph.stores.duckdb.base import DuckDBStoreBase


class InfographicStoreDuckDB(DuckDBStoreBase, AbstractInfographicStore):
    table_name = "infographics"
    create_table_sql = """
        CREATE TABLE IF NOT EXISTS infographics (
            infographic_id TEXT PRIMARY KEY,
            session_id TEXT NOT NULL,
            image_path TEXT NOT NULL,
            template_type TEXT NOT NULL,
            layout_data JSON NOT NULL,
            created_at BIGINT NOT NULL
        )
    """

    def create_infographic(self, infographic_data: InfographicCreate) -> Infographic:
        infographic_id = uuid.uuid4().hex
        created_at = int(time.time())
        self.execute(
            "INSERT INTO infographics (infographic_id, session_id, image_path, template_type, layout_data, created_at) VALUES (?, ?, ?, ?, ?, ?)",
            (
                infographic_id,
                infographic_data.session_id,
                "",
                infographic_data.template_type,
                str(infographic_data.layout_data),
                created_at,
            ),
        )
        return Infographic(
            infographic_id=infographic_id,
            session_id=infographic_data.session_id,
            image_path="",
            template_type=infographic_data.template_type,
            layout_data=infographic_data.layout_data,
            created_at=created_at,
        )

    def get_infographic(self, session_id: str) -> Infographic | None:
        cursor = self.execute(
            "SELECT infographic_id, session_id, image_path, template_type, layout_data, created_at FROM infographics WHERE session_id = ? ORDER BY created_at DESC LIMIT 1",
            (session_id,),
        )
        row = cursor.fetchone()
        if not row:
            return None
        return Infographic(
            infographic_id=row[0],
            session_id=row[1],
            image_path=row[2],
            template_type=row[3],
            layout_data=row[4],
            created_at=row[5],
        )

    def delete_infographic(self, infographic_id: str) -> bool:
        cursor = self.execute("DELETE FROM infographics WHERE infographic_id = ?", (infographic_id,))
        return getattr(cursor, "rowcount", 0) != 0
