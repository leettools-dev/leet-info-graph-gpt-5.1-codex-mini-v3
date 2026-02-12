import os
import tempfile

from jose import jwt
from fastapi.testclient import TestClient

from infograph.svc.api_service import create_app
from infograph.stores.duckdb.duckdb_client import DuckDBClient
from infograph.stores.duckdb.user_store_duckdb import UserStoreDuckDB
from infograph.core.schemas.user import UserCreate


def test_auth_me_endpoint():
    # Use a temp database for isolation
    tmpdir = tempfile.TemporaryDirectory()
    db_path = os.path.join(tmpdir.name, "infograph_test.db")
    os.environ["DATABASE_PATH"] = db_path
    # Ensure JWT secret is known
    os.environ.setdefault("JWT_SECRET", "secret")

    # Create a user directly in the DB
    client = DuckDBClient(db_path)
    user_store = UserStoreDuckDB(client)
    user_create = UserCreate(email="alice@example.com", name="Alice", google_id="google-sub-123")
    user = user_store.create_user(user_create)

    # Create a JWT for that user using same secret/algorithm as AuthService
    token = jwt.encode({"sub": user.user_id, "email": user.email, "name": user.name}, os.environ["JWT_SECRET"], algorithm="HS256")

    app = create_app()
    test_client = TestClient(app)

    headers = {"Authorization": f"Bearer {token}"}
    resp = test_client.get("/api/v1/auth/me", headers=headers)
    assert resp.status_code == 200
    data = resp.json()
    assert data["email"] == "alice@example.com"
    assert data["name"] == "Alice"
    assert data["user_id"] == user.user_id

    tmpdir.cleanup()
