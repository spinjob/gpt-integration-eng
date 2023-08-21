import pytest
from api_client import APIClient

def test_api_client_init():
    client = APIClient()
    assert client is not None

@pytest.mark.parametrize("endpoint, data, expected", [
    ("createOrder", {"test": "data"}, True),
    ("updateOrderStatus", {"test": "data"}, True),
    ("getMenu", {"test": "data"}, True),
    ("publishError", {"test": "data"}, True),
])
def test_api_client_request(endpoint, data, expected):
    client = APIClient()
    assert client.request(endpoint, data) == expected
