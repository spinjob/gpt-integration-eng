import pytest
from oauth2_client import OAuth2Client

def test_get_access_token():
    client = OAuth2Client(client_id='test', client_secret='test', scope='test', grant_type='client_credentials')
    token = client.get_access_token()
    assert isinstance(token, str)

def test_refresh_access_token():
    client = OAuth2Client(client_id='test', client_secret='test', scope='test', grant_type='client_credentials')
    token = client.refresh_access_token()
    assert isinstance(token, str)
