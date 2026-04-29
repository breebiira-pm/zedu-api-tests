import requests

def test_photos_endpoint():
    response = requests.get("https://jsonplaceholder.typicode.com/photos")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0
    assert "url" in data[0]
