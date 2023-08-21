import pytest
from webhook_handler import WebhookHandler

def test_handle_request():
    handler = WebhookHandler()
    request = {"method": "POST", "body": {"order": {"id": "123", "status": "NEW"}}}
    handler.handle_request(request)
    assert handler.request == request
