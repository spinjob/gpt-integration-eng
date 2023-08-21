import pytest
from oauth2_authenticator import OAuth2Authenticator

def test_authenticate():
    authenticator = OAuth2Authenticator()
    credentials = {"client_id": "abc", "client_secret": "def"}
    token = authenticator.authenticate(credentials)
    assert isinstance(token, str)
