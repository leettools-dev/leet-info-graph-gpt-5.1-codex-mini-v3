from __future__ import annotations

from pathlib import Path

import pytest

from infograph.core.schemas.infographic import InfographicCreate
from infograph.core.schemas.message import MessageCreate
from infograph.core.schemas.research_session import ResearchSessionCreate
from infograph.core.schemas.source import SourceCreate
from infograph.core.schemas.user import UserCreate
from infograph.stores.duckdb import (
    DuckDBClient,
    InfographicStoreDuckDB,
    MessageStoreDuckDB,
    SessionStoreDuckDB,
    SourceStoreDuckDB,
    UserStoreDuckDB,
)


@pytest.fixture

def duckdb_client(tmp_path: Path) -> DuckDBClient:
    db_path = tmp_path / "infograph.db"
    return DuckDBClient(str(db_path))


@pytest.fixture

def stores(duckdb_client: DuckDBClient) -> dict[str, object]:
    user_store = UserStoreDuckDB(duckdb_client)
    session_store = SessionStoreDuckDB(duckdb_client)
    source_store = SourceStoreDuckDB(duckdb_client)
    message_store = MessageStoreDuckDB(duckdb_client)
    infographic_store = InfographicStoreDuckDB(duckdb_client)

    return {
        "user_store": user_store,
        "session_store": session_store,
        "source_store": source_store,
        "message_store": message_store,
        "infographic_store": infographic_store,
    }


def _create_user(user_store: UserStoreDuckDB, suffix: str = "1"):
    return user_store.create_user(
        UserCreate(email=f"user{suffix}@example.com", name="Tester", google_id=f"gid-{suffix}")
    )


def test_user_store_crud(stores: dict[str, object]) -> None:
    user_store: UserStoreDuckDB = stores["user_store"]  # type: ignore[assignment]
    created_user = _create_user(user_store)

    fetched = user_store.get_user(created_user.user_id)
    assert fetched is not None
    assert fetched.user_id == created_user.user_id

    by_email = user_store.get_user_by_email(created_user.email)
    assert by_email is not None
    assert by_email.email == created_user.email

    all_users = list(user_store.list_users(limit=10))
    assert created_user.user_id in {user.user_id for user in all_users}


def test_session_store_roundtrip(stores: dict[str, object]) -> None:
    user_store: UserStoreDuckDB = stores["user_store"]  # type: ignore[assignment]
    session_store: SessionStoreDuckDB = stores["session_store"]  # type: ignore[assignment]

    user = _create_user(user_store, suffix="session")
    session = session_store.create_session(user.user_id, ResearchSessionCreate(prompt="Research everything"))

    fetched = session_store.get_session(session.session_id)
    assert fetched is not None
    assert fetched.session_id == session.session_id

    listings = list(session_store.list_sessions(user.user_id, limit=5))
    assert any(item.session_id == session.session_id for item in listings)

    assert session_store.delete_session(session.session_id)
    assert session_store.get_session(session.session_id) is None


def test_source_store_crud(stores: dict[str, object]) -> None:
    user_store: UserStoreDuckDB = stores["user_store"]  # type: ignore[assignment]
    session_store: SessionStoreDuckDB = stores["session_store"]  # type: ignore[assignment]
    source_store: SourceStoreDuckDB = stores["source_store"]  # type: ignore[assignment]

    user = _create_user(user_store, suffix="source")
    session = session_store.create_session(user.user_id, ResearchSessionCreate(prompt="Find sources"))

    source = source_store.add_source(
        SourceCreate(
            session_id=session.session_id,
            title="Example Source",
            url="https://example.com",
            snippet="Snippet text",
            confidence=0.78,
        )
    )

    assert source_store.get_source(source.source_id) is not None
    assert any(item.session_id == session.session_id for item in source_store.list_sources(session.session_id))


def test_message_store_persistence(stores: dict[str, object]) -> None:
    user_store: UserStoreDuckDB = stores["user_store"]  # type: ignore[assignment]
    session_store: SessionStoreDuckDB = stores["session_store"]  # type: ignore[assignment]
    message_store: MessageStoreDuckDB = stores["message_store"]  # type: ignore[assignment]

    user = _create_user(user_store, suffix="message")
    session = session_store.create_session(user.user_id, ResearchSessionCreate(prompt="Chat"))

    message = message_store.add_message(
        MessageCreate(session_id=session.session_id, role="user", content="Hello")
    )

    fetched = message_store.get_message(message.message_id)
    assert fetched is not None
    assert fetched.content == "Hello"

    messages = list(message_store.list_messages(session.session_id, limit=10))
    assert any(item.message_id == message.message_id for item in messages)


def test_infographic_store_relations(stores: dict[str, object]) -> None:
    user_store: UserStoreDuckDB = stores["user_store"]  # type: ignore[assignment]
    session_store: SessionStoreDuckDB = stores["session_store"]  # type: ignore[assignment]
    infographic_store: InfographicStoreDuckDB = stores["infographic_store"]  # type: ignore[assignment]

    user = _create_user(user_store, suffix="infographic")
    session = session_store.create_session(
        user.user_id,
        ResearchSessionCreate(prompt="Create infographic"),
    )

    infographic = infographic_store.create_infographic(
        InfographicCreate(
            session_id=session.session_id,
            image_path="/tmp/infographic.png",
            template_type="basic",
            layout_data={"title": "Insight"},
        )
    )

    fetched = infographic_store.get_infographic(session.session_id)
    assert fetched is not None
    assert fetched.layout_data["title"] == "Insight"

    listings = infographic_store.list_infographics(user.user_id)
    assert any(item.infographic_id == infographic.infographic_id for item in listings)
