import pytest
from webhook_handler import WebhookHandler

def test_handle_webhook():
    handler = WebhookHandler()
    response = handler.handle_webhook({'test': 'data'})
    assert response.status_code == 200
