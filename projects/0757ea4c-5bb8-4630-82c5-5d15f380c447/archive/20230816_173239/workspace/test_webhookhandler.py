import pytest
from webhookhandler import WebhookHandler

def test_webhook_received():
    handler = WebhookHandler()
    response = handler.handle_webhook({'key': 'value'})
    assert response.status_code == 200
