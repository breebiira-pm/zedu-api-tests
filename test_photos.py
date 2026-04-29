import requests

def test_photos_endpoint():
    response = requests.get("https://jsonplaceholder.typicode.com/photos")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0
    assert "url" in data[0]
import requests

def test_first_photo_details():
    response = requests.get("https://jsonplaceholder.typicode.com/photos/1")
    assert response.status_code == 200
    data = response.json()
    # Check that the first photo has the expected ID and valid fields
    assert data["id"] == 1
    assert isinstance(data["title"], str)
    assert len(data["title"]) > 0
    assert isinstance(data["url"], str)
    assert data["url"].startswith("http")
    assert isinstance(data["thumbnailUrl"], str)
    assert data["thumbnailUrl"].startswith("http")
