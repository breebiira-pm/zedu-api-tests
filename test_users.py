import requests

def test_user_endpoint():
    response = requests.get("https://jsonplaceholder.typicode.com/users/1")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 1
    assert "username" in data
import requests

def test_first_user_details():
    response = requests.get("https://jsonplaceholder.typicode.com/users/1")
    assert response.status_code == 200
    data = response.json()
    # Check that the first user has the expected ID and valid fields
    assert data["id"] == 1
    assert isinstance(data["name"], str)
    assert len(data["name"]) > 0
    assert isinstance(data["email"], str)
    assert "@" in data["email"]
