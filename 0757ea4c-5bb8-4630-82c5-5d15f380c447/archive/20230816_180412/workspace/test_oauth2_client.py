import pytest
from oauth2_client import OAuth2Client

def test_get_token():
    client = OAuth2Client()
    token = client.get_token()
    assert token is not None

def test_request():
    client = OAuth2Client()
    response = client.request("GET", "/orders", {}, {})
    assert response.status_code == 200
