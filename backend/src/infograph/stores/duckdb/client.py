from __future__ import annotations

import os
from pathlib import Path
from typing import Iterable

import duckdb

DEFAULT_DB_ENV = "DATABASE_PATH"
DEFAULT_DB_DIR = Path("/workspace/data/duckdb")


class DuckDBClient:
    """Simple DuckDB client used by store implementations."""

    def __init__(self, db_path: str | Path | None = None) -> None:
        if db_path is None:
            db_dir = Path(os.environ.get(DEFAULT_DB_ENV, DEFAULT_DB_DIR))
            db_dir.mkdir(parents=True, exist_ok=True)
            db_path = db_dir / "infograph.db"
        else:
            db_path = Path(db_path)
            db_path.parent.mkdir(parents=True, exist_ok=True)

        self.db_path = db_path
        self.connection = duckdb.connect(str(self.db_path))
        self.connection.execute("PRAGMA threads=1")

    def execute(self, sql: str, parameters: Iterable | None = None) -> duckdb.DuckDBPyConnection:
        if parameters is None:
            return self.connection.execute(sql)
        return self.connection.execute(sql, parameters)

    def close(self) -> None:
        self.connection.close()
