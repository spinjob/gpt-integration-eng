import pytest
from oauth2_client import OAuth2Client

def test_generate_token():
    client = OAuth2Client(client_id='test_id', client_secret='test_secret', token_url='test_url')
    token = client.generate_token()
    assert isinstance(token, str)

def test_refresh_token():
    client = OAuth2Client(client_id='test_id', client_secret='test_secret', token_url='test_url')
    client.generate_token()
    client.refresh_token()
    assert isinstance(client.token, str)
