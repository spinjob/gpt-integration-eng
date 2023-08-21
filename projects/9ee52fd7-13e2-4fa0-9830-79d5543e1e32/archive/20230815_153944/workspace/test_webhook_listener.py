import pytest
from webhook_listener import WebhookListener

def test_listen():
    listener = WebhookListener()
    assert listener.listen() == True, "Webhook listener should start successfully"
