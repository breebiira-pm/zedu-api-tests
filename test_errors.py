import requests

def test_invalid_user():
    response = requests.get("https://jsonplaceholder.typicode.com/users/9999")
    # Expecting a 404 Not Found
    assert response.status_code == 404
import requests

def test_invalid_post():
    response = requests.get("https://jsonplaceholder.typicode.com/posts/9999")
    # Expecting a 404 Not Found
    assert response.status_code == 404
