import pytest
from http_requester import HttpRequester

def test_send_request():
    requester = HttpRequester()
    api_id = "2389bc50-2646-4e94-bb34-86c9ea23cd7e"
    method = "GET"
    path = "/menu"
    headers = {"Authorization": "Bearer test-token"}
    body = None
    response = requester.send_request(api_id, method, path, headers, body)
    assert isinstance(response, dict)
