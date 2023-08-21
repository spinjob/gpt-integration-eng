import pytest
from webhookhandler import WebhookHandler

def test_handle_webhook():
    handler = WebhookHandler()
    webhook_body = {"metadata": {"storeId": "test-store-id"}}
    result = handler.handle_webhook(webhook_body)
    assert result == "test-store-id"
