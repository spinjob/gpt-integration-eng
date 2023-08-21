import pytest
from api import API

def test_request():
    api = API()
    response = api.request("GET", "/orders", {}, {})
    assert response.status_code == 200
