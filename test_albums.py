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
