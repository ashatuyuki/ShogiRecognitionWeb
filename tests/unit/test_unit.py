from starlette.testclient import TestClient

from app.main import app


def test_ping():
    """
    GIVEN
    WHEN health check with GET
    THEN response with status 200 is returned
    """
    client = TestClient(app)
    response = client.get("/")
    assert response.status_code == 200


def test_contents():
    """
    GIVEN
    WHEN health check with GET
    THEN correct title and some ...(TBD) are returned
    """
    client = TestClient(app)
    response = client.get("/")
    assert b"<title>Shogi Diagram Converter" in response.content
