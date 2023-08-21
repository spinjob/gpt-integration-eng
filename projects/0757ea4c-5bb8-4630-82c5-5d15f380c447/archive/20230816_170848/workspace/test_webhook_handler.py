import pytest
from webhook_handler import WebhookHandler

def test_handle_webhook():
    handler = WebhookHandler()
    result = handler.handle_webhook('test_webhook_data')
    assert result is not None
