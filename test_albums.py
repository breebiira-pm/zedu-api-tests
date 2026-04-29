import requests

def test_albums_endpoint():
    response = requests.get("https://jsonplaceholder.typicode.com/albums")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0
    assert "title" in data[0]
