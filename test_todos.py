import requests

def test_todos_endpoint():
    response = requests.get("https://jsonplaceholder.typicode.com/todos")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0
    assert "title" in data[0]
import requests

def test_user_for_first_todo():
    # First, get the first todo
    todo_response = requests.get("https://jsonplaceholder.typicode.com/todos/1")
    assert todo_response.status_code == 200
    todo_data = todo_response.json()
    user_id = todo_data["userId"]

    # Then, use that user_id to get the user
    user_response = requests.get(f"https://jsonplaceholder.typicode.com/users/{user_id}")
    assert user_response.status_code == 200
    user_data = user_response.json()
    assert user_data["id"] == user_id
    assert "name" in user_data
    assert "email" in user_data
import requests

def test_first_todo_details():
    response = requests.get("https://jsonplaceholder.typicode.com/todos/1")
    assert response.status_code == 200
    data = response.json()
    # Check that the first todo has the expected ID and valid fields
    assert data["id"] == 1
    assert isinstance(data["title"], str)
    assert len(data["title"]) > 0
    assert isinstance(data["completed"], bool)
import requests

def test_todos_filter_by_userId():
    response = requests.get("https://jsonplaceholder.typicode.com/todos?userId=1")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0
    # Every todo should belong to userId = 1
    for todo in data:
        assert todo["userId"] == 1
        assert isinstance(todo["title"], str)
        assert isinstance(todo["completed"], bool)
import requests

def test_todos_filter_by_userId():
    response = requests.get("https://jsonplaceholder.typicode.com/todos?userId=1")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0
    for todo in data:
        assert todo["userId"] == 1
        assert isinstance(todo["title"], str)
        assert isinstance(todo["completed"], bool)
