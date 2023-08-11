from api_client import APIClient

def test_fetch_data():
    api_client = APIClient()
    data = api_client.fetch_data()
    assert isinstance(data, list)
