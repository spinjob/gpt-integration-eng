import pytest
from webhook_handler import WebhookHandler

def test_webhook_handler():
    webhook_handler = WebhookHandler()
    assert webhook_handler.handle_webhook() is None
