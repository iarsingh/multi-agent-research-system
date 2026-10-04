from fastapi.testclient import TestClient
from maresearch.main import app

client = TestClient(app)


def test_runs_and_refuses_a_write():
    payload = client.post("/agent/run", json={"goal": 'research rollback policy', **{'payload': {}}}).json()
    assert payload["refused"] is False
    assert payload["applied"] is False
    assert payload["roles"] == ["researcher", "critic"]
    refused = client.post("/agent/run", json={"goal": 'deploy the report'}).json()
    assert refused["refused"] is True
