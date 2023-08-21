import pytest
from webhookhandler import WebhookHandler

def test_handle_webhook():
    handler = WebhookHandler()
    data = {'key': 'value'}
    result = handler.handle_webhook(data)
    assert result == 'Webhook handled'
