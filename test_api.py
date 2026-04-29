import requests

def test_example_api():
    response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
    assert response.status_code == 200
    data = response.json()
    assert "title" in data
def test_second_post():
    response = requests.get("https://jsonplaceholder.typicode.com/posts/2")
    assert response.status_code == 200
    data = response.json()
    assert "title" in data
    assert data["id"] == 2
def test_user_endpoint():
    response = requests.get("https://jsonplaceholder.typicode.com/users/1")
    assert response.status_code == 200
    data = response.json()
    assert "name" in data
    assert "email" in data
    assert data["id"] == 1
