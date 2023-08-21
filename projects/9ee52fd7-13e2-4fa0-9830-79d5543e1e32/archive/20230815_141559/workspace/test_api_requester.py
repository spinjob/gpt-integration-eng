import pytest
from api_requester import APIRequester

def test_request():
    requester = APIRequester()
    method = "GET"
    url = "https://example.com"
    headers = {"Authorization": "Bearer xyz"}
    body = None
    response = requester.request(method, url, headers, body)
    assert isinstance(response, dict)
