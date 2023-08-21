import pytest
from webhook_handler import WebhookHandler

def test_handle_trigger():
    handler = WebhookHandler()
    request = {"body": {"metadata": {"storeId": "123"}}}
    data = handler.handle_trigger(request)
    assert data == {"storeId": "123"}
