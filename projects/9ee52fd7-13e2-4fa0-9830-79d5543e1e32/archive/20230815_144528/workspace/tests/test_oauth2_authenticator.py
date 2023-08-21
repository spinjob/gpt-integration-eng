import pytest
from oauth2_authenticator import OAuth2Authenticator

def test_authenticate():
    authenticator = OAuth2Authenticator()
    api_id = "2389bc50-2646-4e94-bb34-86c9ea23cd7e"
    token = authenticator.authenticate(api_id)
    assert isinstance(token, str)
