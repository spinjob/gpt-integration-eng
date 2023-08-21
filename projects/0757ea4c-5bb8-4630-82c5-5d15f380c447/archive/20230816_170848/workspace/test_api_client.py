import pytest
from api_client import APIClient

def test_create_order():
    client = APIClient()
    result = client.create_order('test_order_data')
    assert result is not None

def test_update_order_status():
    client = APIClient()
    result = client.update_order_status('test_order_id', 'test_status')
    assert result is not None

def test_get_menu():
    client = APIClient()
    result = client.get_menu()
    assert result is not None

def test_publish_error():
    client = APIClient()
    result = client.publish_error('test_error_data')
    assert result is not None
