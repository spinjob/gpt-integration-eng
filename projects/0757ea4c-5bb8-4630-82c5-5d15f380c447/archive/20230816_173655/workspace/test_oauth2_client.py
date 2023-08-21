import pytest
from oauth2_client import OAuth2Client

def test_generate_token():
    client = OAuth2Client(client_id='test_id', client_secret='test_secret', token_url='https://test.com/token')
    token = client.generate_token()
    assert 'access_token' in token

def test_refresh_token():
    client = OAuth2Client(client_id='test_id', client_secret='test_secret', token_url='https://test.com/token')
    token = client.refresh_token()
    assert 'access_token' in token
