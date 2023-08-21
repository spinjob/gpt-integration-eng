import pytest
from api_client import APIClient

def test_api_client():
    api_client = APIClient()
    assert api_client.make_request() is None
