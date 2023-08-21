import pytest
from main import get_config, run_workflow, handle_webhook

def test_get_config():
    config = get_config()
    assert 'client_id' in config
    assert 'client_secret' in config
    assert 'scope' in config
    assert 'grant_type' in config

def test_run_workflow():
    response = run_workflow('order_data')
    assert response.status_code == 200

def test_handle_webhook():
    response = handle_webhook('webhook_data')
    assert response.status_code == 200
