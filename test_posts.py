import requests

def test_example_api():
    response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 1

def test_second_post():
    response = requests.get("https://jsonplaceholder.typicode.com/posts/2")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 2
