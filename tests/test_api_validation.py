from utils.api_client import APIClient

def test_get_user():
    response = APIClient.get("/users/1")

    assert response.status_code == 200
    assert response.json()["id"] == 1
