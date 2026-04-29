import requests

def test_comments_endpoint():
    response = requests.get("https://jsonplaceholder.typicode.com/comments?postId=1")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0
    assert "email" in data[0]
import requests

def test_comments_for_first_post():
    # First, get the first post
    post_response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
    assert post_response.status_code == 200
    post_data = post_response.json()
    post_id = post_data["id"]

    # Then, use that post_id to get comments
    comments_response = requests.get(f"https://jsonplaceholder.typicode.com/comments?postId={post_id}")
    assert comments_response.status_code == 200
    comments_data = comments_response.json()
    assert isinstance(comments_data, list)
    assert len(comments_data) > 0
    assert "email" in comments_data[0]
import requests

def test_first_comment_details():
    response = requests.get("https://jsonplaceholder.typicode.com/comments/1")
    assert response.status_code == 200
    data = response.json()
    # Check that the first comment has the expected ID and valid fields
    assert data["id"] == 1
    assert isinstance(data["name"], str)
    assert len(data["name"]) > 0
    assert isinstance(data["email"], str)
    assert "@" in data["email"]
    assert isinstance(data["body"], str)
    assert len(data["body"]) > 0
import requests

def test_comments_filter_by_postId():
    response = requests.get("https://jsonplaceholder.typicode.com/comments?postId=1")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0
    # Every comment should belong to postId = 1
    for comment in data:
        assert comment["postId"] == 1
        assert "email" in comment
        assert "@" in comment["email"]
