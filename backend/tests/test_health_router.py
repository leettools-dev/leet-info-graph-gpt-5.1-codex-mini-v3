import os
import sys
import pytest

# Ensure backend/src is on PYTHONPATH for tests
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))
from fastapi.testclient import TestClient

from infograph.svc.api_service import create_app


@pytest.fixture

def client() -> TestClient:
    return TestClient(create_app())


def test_health_endpoint(client: TestClient) -> None:
    response = client.get("/api/v1/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok", "version": "1.0.0"}
