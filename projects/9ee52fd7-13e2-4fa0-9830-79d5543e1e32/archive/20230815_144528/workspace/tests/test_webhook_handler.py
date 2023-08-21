import pytest
from webhook_handler import WebhookHandler

def test_handle_request():
    handler = WebhookHandler()
    request = {"body": {"metadata": {"storeId": "test-store-id"}}}
    data = handler.handle_request(request)
    assert data == {"metadata": {"storeId": "test-store-id"}}
