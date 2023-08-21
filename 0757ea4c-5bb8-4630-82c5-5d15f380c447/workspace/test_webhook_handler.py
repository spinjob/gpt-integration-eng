import pytest
from webhook_handler import WebhookHandler

def test_parse_request_body():
    handler = WebhookHandler()
    request_body = '{"key": "value"}'
    data = handler.parse_request_body(request_body)
    assert data == {"key": "value"}

def test_trigger_workflow():
    handler = WebhookHandler()
    data = {"key": "value"}
    assert handler.trigger_workflow(data) is None
