import pytest
from fastapi.testclient import TestClient

from infograph.svc.api_service import create_app


@pytest.fixture

def client() -> TestClient:
    return TestClient(create_app())


def test_health_endpoint(client: TestClient) -> None:
    response = client.get("/api/v1/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok", "version": "1.0.0"}
