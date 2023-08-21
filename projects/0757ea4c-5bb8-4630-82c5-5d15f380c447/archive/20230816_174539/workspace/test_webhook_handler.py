import pytest
from webhook_handler import WebhookHandler

def test_parse_webhook():
    webhook_handler = WebhookHandler()
    webhook_data = {"metadata": {"payload": {"currencyCode": "USD"}}}
    parsed_data = webhook_handler.parse_webhook(webhook_data)
    assert parsed_data == {"currencyCode": "USD"}
