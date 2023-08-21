import pytest
from oauth2_client import OAuth2Client

def test_get_access_token():
    client = OAuth2Client(client_id='test_id', client_secret='test_secret', token_url='https://test.com/token')
    token = client.get_access_token()
    assert token is not None

def test_refresh_access_token():
    client = OAuth2Client(client_id='test_id', client_secret='test_secret', token_url='https://test.com/token')
    token = client.refresh_access_token()
    assert token is not None
