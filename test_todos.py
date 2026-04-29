import requests

def test_todos_endpoint():
    response = requests.get("https://jsonplaceholder.typicode.com/todos")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0
    assert "title" in data[0]
