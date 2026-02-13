import os
import tempfile
from unittest.mock import patch

from fastapi.testclient import TestClient

from infograph.svc.api_service import create_app
from infograph.core.schemas.user import UserCreate
from infograph.stores.duckdb.duckdb_client import DuckDBClient
from infograph.stores.duckdb.user_store_duckdb import UserStoreDuckDB


def test_exchange_google_token_creates_user_and_returns_jwt():
    tmpdir = tempfile.TemporaryDirectory()
    db_path = os.path.join(tmpdir.name, "infograph_test.db")
    os.environ["DATABASE_PATH"] = db_path
    os.environ.setdefault("JWT_SECRET", "secret")
    os.environ.setdefault("GOOGLE_CLIENT_ID", "test-client-id")

    # Prepare app
    app = create_app()
    client = TestClient(app)

    # Patch the google token verifier to return a predictable user payload
    fake_user = UserCreate(email="bob@example.com", name="Bob", google_id="google-sub-1")

    with patch("infograph.services.auth_service.id_token.verify_oauth2_token") as mock_verify:
        mock_verify.return_value = {
            "email": fake_user.email,
            "name": fake_user.name,
            "sub": fake_user.google_id,
            "iss": "https://accounts.google.com",
        }

        resp = client.post(
            "/api/v1/auth/google",
            json={"credential": "fake-credential-token"},
        )

    assert resp.status_code == 200
    data = resp.json()
    assert "token" in data
    assert data["user"]["email"] == "bob@example.com"

    tmpdir.cleanup()
