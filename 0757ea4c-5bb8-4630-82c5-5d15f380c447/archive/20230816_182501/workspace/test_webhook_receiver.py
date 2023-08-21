import pytest
from webhook_receiver import WebhookReceiver

def test_webhook_receiver_init():
    receiver = WebhookReceiver()
    assert receiver is not None

def test_webhook_receiver_handle_webhook():
    receiver = WebhookReceiver()
    webhook_data = {"test": "data"}
    assert receiver.handle_webhook(webhook_data) == True
