from __future__ import annotations

from abc import ABC
from typing import Iterable

from infograph.stores.duckdb.client import DuckDBClient


class DuckDBStoreBase(ABC):
    """Base class that ensures the DuckDB table is available for each store."""

    table_name: str
    create_table_sql: str

    def __init__(self, client: DuckDBClient | None = None) -> None:
        self.client = client or DuckDBClient()
        self._ensure_table()

    def _ensure_table(self) -> None:
        self.client.execute(self.create_table_sql)

    def execute(self, sql: str, params: Iterable | None = None):
        return self.client.execute(sql, params)
