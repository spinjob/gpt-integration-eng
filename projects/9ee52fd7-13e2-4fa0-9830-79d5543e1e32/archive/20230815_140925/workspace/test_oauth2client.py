import pytest
from oauth2client import OAuth2Client

def test_get_access_token():
    client = OAuth2Client(client_id='test', client_secret='test', token_url='https://example.com/token')
    token = client.get_access_token()
    assert 'access_token' in token

def test_refresh_access_token():
    client = OAuth2Client(client_id='test', client_secret='test', token_url='https://example.com/token')
    token = client.refresh_access_token()
    assert 'access_token' in token
