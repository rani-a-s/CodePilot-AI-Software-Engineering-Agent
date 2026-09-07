from fastapi.testclient import TestClient

from backend.app.main import app


client = TestClient(app)


def test_root():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json()["message"] == (
        "CodePilot AI Software Engineering Agent is running"
    )


def test_health():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json()["status"] == "healthy"


def test_semantic_search():
    response = client.get(
        "/semantic-search",
        params={
            "query": "find the function that checks if the API is healthy",
            "limit": 3,
        },
    )

    assert response.status_code == 200

    data = response.json()

    assert data["query"] == (
        "find the function that checks if the API is healthy"
    )

    assert len(data["results"]) > 0
    assert data["results"][0]["symbol"] == "health_check"


def test_codepilot_agent():
    response = client.get(
        "/ask",
        params={
            "question": "Where is the API health check implemented?",
            "limit": 3,
        },
    )

    assert response.status_code == 200

    data = response.json()

    assert "health_check" in data["answer"]
    assert "backend/app/main.py" in data["answer"]
    assert len(data["sources"]) > 0