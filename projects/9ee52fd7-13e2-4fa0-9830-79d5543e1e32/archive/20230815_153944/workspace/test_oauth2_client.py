import pytest
from oauth2_client import OAuth2Client

def test_request_token():
    client = OAuth2Client()
    assert client.request_token('2389bc50-2646-4e94-bb34-86c9ea23cd7e') == True, "Token request should be successful"

def test_refresh_token():
    client = OAuth2Client()
    assert client.refresh_token('2389bc50-2646-4e94-bb34-86c9ea23cd7e') == True, "Token refresh should be successful"
