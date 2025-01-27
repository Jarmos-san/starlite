import pytest
from starlite import Starlite, MediaType, get
from starlite.status_codes import HTTP_200_OK
from starlite.testing import TestClient


@get(path="/health-check", media_type=MediaType.TEXT)
def health_check() -> str:
    return "healthy"


app = Starlite(route_handlers=[health_check])


def test_health_check():
    with TestClient(app=app) as client:
        response = client.get("/health-check")
        assert response.status_code == HTTP_200_OK
        assert response.text == "healthy"


@pytest.fixture(scope="function")
def test_client() -> TestClient:
    return TestClient(app=app)


def test_health_check_with_fixture(test_client: TestClient):
    with test_client as client:
        response = client.get("/health-check")
        assert response.status_code == HTTP_200_OK
        assert response.text == "healthy"
