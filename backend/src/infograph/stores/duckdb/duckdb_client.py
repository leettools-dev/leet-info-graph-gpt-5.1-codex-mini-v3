from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Iterable

import duckdb


class DuckDBClient:
    """Minimal DuckDB wrapper for Infograph stores."""

    def __init__(self, db_path: str) -> None:
        path = Path(db_path)
        path.parent.mkdir(parents=True, exist_ok=True)
        self._conn = duckdb.connect(str(path))
        self._json_adapter_registered = False

    def execute(self, query: str, parameters: Iterable[Any] | None = None) -> duckdb.DuckDBPyConnection:
        if parameters is None:
            return self._conn.execute(query)
        return self._conn.execute(query, parameters)

    def register_json_adapter(self) -> None:
        if self._json_adapter_registered:
            return
        duckdb.register_adapter(dict, lambda value: json.dumps(value))
        self._json_adapter_registered = True

    def fetch_one(self, query: str, parameters: Iterable[Any] | None = None) -> dict[str, Any] | None:
        cursor = self.execute(query, parameters)
        row = cursor.fetchone()
        if row is None or cursor.description is None:
            return None
        return self._row_to_dict(row, cursor.description)

    def fetch_all(self, query: str, parameters: Iterable[Any] | None = None) -> list[dict[str, Any]]:
        cursor = self.execute(query, parameters)
        rows = cursor.fetchall()
        if cursor.description is None:
            return []
        return [self._row_to_dict(row, cursor.description) for row in rows]

    @staticmethod
    def _row_to_dict(row: tuple[Any, ...], description: tuple[tuple[str, Any], ...]) -> dict[str, Any]:
        columns = [col[0] for col in description]
        return {column: value for column, value in zip(columns, row)}

