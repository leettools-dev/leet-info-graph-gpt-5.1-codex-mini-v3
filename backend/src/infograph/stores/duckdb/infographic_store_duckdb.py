from __future__ import annotations

from infograph.core.schemas.infographic import Infographic, InfographicCreate
from infograph.stores.abstract_infographic_store import AbstractInfographicStore
from infograph.stores.duckdb.duckdb_client import DuckDBClient


class InfographicStoreDuckDB(AbstractInfographicStore):
    """DuckDB-backed Infographic store."""

    _TABLE_NAME = "infographics"
    _CREATE_TABLE_SQL = f"""
    CREATE TABLE IF NOT EXISTS { _TABLE_NAME } (
        infographic_id TEXT PRIMARY KEY,
        session_id TEXT NOT NULL,
        image_path TEXT NOT NULL,
        template_type TEXT NOT NULL,
        layout_data TEXT NOT NULL,
        created_at INTEGER NOT NULL
    )
    """

    def __init__(self, client: DuckDBClient) -> None:
        self._client = client
        self._client.register_json_adapter()
        self._client.execute(self._CREATE_TABLE_SQL)

    def create_infographic(self, infographic_create: InfographicCreate) -> Infographic:
        infographic = Infographic.from_create(infographic_create)
        self._client.execute(
            f"INSERT INTO {self._TABLE_NAME} (infographic_id, session_id, image_path, template_type, layout_data, created_at)"
            " VALUES (?, ?, ?, ?, ?, ?)",
            (
                infographic.infographic_id,
                infographic.session_id,
                infographic.image_path,
                infographic.template_type,
                infographic.layout_data,
                infographic.created_at,
            ),
        )
        return infographic

    def get_infographic(self, session_id: str) -> Infographic | None:
        row = self._client.fetch_one(
            f"SELECT * FROM {self._TABLE_NAME} WHERE session_id = ?",
            (session_id,),
        )
        return self._row_to_infographic(row)

    def list_infographics(self, user_id: str) -> list[Infographic]:
        rows = self._client.fetch_all(
            f"SELECT i.* FROM {self._TABLE_NAME} i JOIN sessions s ON i.session_id = s.session_id WHERE s.user_id = ?",
            (user_id,),
        )
        return [self._row_to_infographic(row) for row in rows if row is not None]

    @staticmethod
    def _row_to_infographic(row: dict[str, object] | None) -> Infographic | None:
        if row is None:
            return None
        return Infographic.model_validate(row)
