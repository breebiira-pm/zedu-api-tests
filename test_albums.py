import requests

def test_albums_endpoint():
    response = requests.get("https://jsonplaceholder.typicode.com/albums")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0
    assert "title" in data[0]
import requests

def test_photos_for_first_album():
    # First, get the first album
    album_response = requests.get("https://jsonplaceholder.typicode.com/albums/1")
    assert album_response.status_code == 200
    album_data = album_response.json()
    album_id = album_data["id"]

    # Then, use that album_id to get photos
    photos_response = requests.get(f"https://jsonplaceholder.typicode.com/photos?albumId={album_id}")
    assert photos_response.status_code == 200
    photos_data = photos_response.json()
    assert isinstance(photos_data, list)
    assert len(photos_data) > 0
    assert "url" in photos_data[0]
import requests

def test_photos_for_first_album():
    # First, get the first album
    album_response = requests.get("https://jsonplaceholder.typicode.com/albums/1")
    assert album_response.status_code == 200
    album_data = album_response.json()
    album_id = album_data["id"]

    # Then, use that album_id to get photos
    photos_response = requests.get(f"https://jsonplaceholder.typicode.com/photos?albumId={album_id}")
    assert photos_response.status_code == 200
    photos_data = photos_response.json()
    assert isinstance(photos_data, list)
    assert len(photos_data) > 0
    assert "url" in photos_data[0]
import requests

def test_first_album_details():
    response = requests.get("https://jsonplaceholder.typicode.com/albums/1")
    assert response.status_code == 200
    data = response.json()
    # Check that the first album has the expected ID and valid fields
    assert data["id"] == 1
    assert isinstance(data["title"], str)
    assert len(data["title"]) > 0
    assert isinstance(data["userId"], int)
    assert data["userId"] > 0
import requests

def test_album_user_ownership():
    # Get album 1
    album_response = requests.get("https://jsonplaceholder.typicode.com/albums/1")
    assert album_response.status_code == 200
    album_data = album_response.json()
    user_id = album_data["userId"]

    # Verify that userId corresponds to a valid user
    user_response = requests.get(f"https://jsonplaceholder.typicode.com/users/{user_id}")
    assert user_response.status_code == 200
    user_data = user_response.json()
    assert user_data["id"] == user_id
    assert isinstance(user_data["name"], str)
    assert "email" in user_data
