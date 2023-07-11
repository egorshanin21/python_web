from fastapi.testclient import TestClient
import main

client = TestClient(main.app)


def test_read_main():
    response = client.get("/api/healthchecker")
    assert response.status_code == 200



