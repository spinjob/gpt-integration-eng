from api_client import APIClient

def test_fetch_data():
    client = APIClient(url="http://testapi.example.com/data")
    data = client.fetch_data()
    assert data is not None
