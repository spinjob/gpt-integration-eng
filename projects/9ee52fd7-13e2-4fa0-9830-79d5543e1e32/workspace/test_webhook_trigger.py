import pytest
from webhook_trigger import WebhookTrigger

def test_handle_webhook():
    trigger = WebhookTrigger()
    data = {'storeId': 'test_store_id'}
    trigger.handle_webhook(data=data)
    assert trigger.store_id == 'test_store_id'
