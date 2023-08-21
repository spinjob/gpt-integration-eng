import pytest
from api_request_handler import APIRequestHandler

def test_perform_request():
    handler = APIRequestHandler()
    assert handler.perform_request('2389bc50-2646-4e94-bb34-86c9ea23cd7e', {}) == True, "API request should be successful"
