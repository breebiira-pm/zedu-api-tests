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
import requests

def test_posts_for_first_user():
    # First, get the first user
    user_response = requests.get("https://jsonplaceholder.typicode.com/users/1")
    assert user_response.status_code == 200
    user_data = user_response.json()
    user_id = user_data["id"]

    # Then, use that user_id to get posts
    posts_response = requests.get(f"https://jsonplaceholder.typicode.com/posts?userId={user_id}")
    assert posts_response.status_code == 200
    posts_data = posts_response.json()
    assert isinstance(posts_data, list)
    assert len(posts_data) > 0
    assert "title" in posts_data[0]
import requests

def test_first_post_title():
    response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
    assert response.status_code == 200
    data = response.json()
    # Check that the first post has the expected ID and title
    assert data["id"] == 1
    assert data["userId"] == 1
    assert isinstance(data["title"], str)
    assert len(data["title"]) > 0
