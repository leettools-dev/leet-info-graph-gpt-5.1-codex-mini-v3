from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

from fastapi import FastAPI
from fastapi.testclient import TestClient
import pytest

from infograph.core.schemas.research_session import ResearchSessionCreate
from infograph.core.schemas.user import User
from infograph.services.auth_service import AuthService
from infograph.stores.duckdb import DuckDBClient, SessionStoreDuckDB
from infograph.svc.api.v1.routers.session_router import create_session_router


AUTH_TOKEN = "valid-token"


@dataclass
class DummyAuthService:
    user: User
    valid_token: str = AUTH_TOKEN

    def get_user_from_token(self, token: str) -> User:
        if token != self.valid_token:
            raise ValueError("Invalid token")
        return self.user


@pytest.fixture

def user() -> User:
    return User(
        user_id="user-1",
        email="tester@example.com",
        name="Tester",
        google_id="google-1",
        created_at=1,
        updated_at=1,
    )


@pytest.fixture

def session_store(tmp_path: Path) -> SessionStoreDuckDB:
    client = DuckDBClient(str(tmp_path / "sessions.db"))
    return SessionStoreDuckDB(client)


@pytest.fixture

def client(user: User, session_store: SessionStoreDuckDB) -> TestClient:
    app = FastAPI()
    auth_service = DummyAuthService(user=user)
    app.include_router(
        create_session_router(auth_service, session_store),
        prefix="/api/v1",
    )
    return TestClient(app)


def _auth_headers() -> dict[str, str]:
    return {"Authorization": f"Bearer {AUTH_TOKEN}"}


def test_create_and_get_session(client: TestClient) -> None:
    response = client.post(
        "/api/v1/sessions",
        json={"prompt": "Research everything"},
        headers=_auth_headers(),
    )
    assert response.status_code == 200
    payload = response.json()
    assert payload["prompt"] == "Research everything"
    assert payload["status"] == "pending"

    get_resp = client.get(
        f"/api/v1/sessions/{payload['session_id']}",
        headers=_auth_headers(),
    )
    assert get_resp.status_code == 200
    assert get_resp.json()["session_id"] == payload["session_id"]


def test_list_sessions_respects_limit(client: TestClient) -> None:
    for i in range(3):
        client.post(
            "/api/v1/sessions",
            json={"prompt": f"Research {i}"},
            headers=_auth_headers(),
        )

    list_resp = client.get(
        "/api/v1/sessions?limit=2",
        headers=_auth_headers(),
    )
    assert list_resp.status_code == 200
    assert len(list_resp.json()) == 2


def test_delete_session(client: TestClient) -> None:
    create_resp = client.post(
        "/api/v1/sessions",
        json={"prompt": "Disposable research"},
        headers=_auth_headers(),
    )
    session_id = create_resp.json()["session_id"]

    delete_resp = client.delete(
        f"/api/v1/sessions/{session_id}",
        headers=_auth_headers(),
    )
    assert delete_resp.status_code == 200
    assert delete_resp.json()["success"] is True

    missing = client.get(
        f"/api/v1/sessions/{session_id}",
        headers=_auth_headers(),
    )
    assert missing.status_code == 404
