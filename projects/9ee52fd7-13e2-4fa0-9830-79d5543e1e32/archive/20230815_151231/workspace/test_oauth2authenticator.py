import pytest
from oauth2authenticator import OAuth2Authenticator

def test_get_access_token():
    authenticator = OAuth2Authenticator()
    token = authenticator.get_access_token()
    assert isinstance(token, str)

def test_refresh_access_token():
    authenticator = OAuth2Authenticator()
    new_token = authenticator.refresh_access_token("old-token")
    assert isinstance(new_token, str)
