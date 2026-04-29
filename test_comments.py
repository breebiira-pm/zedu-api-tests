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
