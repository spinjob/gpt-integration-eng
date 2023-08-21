import pytest
from api_client import APIClient

def test_create_order():
    api_client = APIClient()
    order_data = {"currencyCode": "USD"}
    response = api_client.create_order(order_data)
    assert response.status_code == 200

def test_update_order_status():
    api_client = APIClient()
    order_id = "123"
    status = "CONFIRMED"
    response = api_client.update_order_status(order_id, status)
    assert response.status_code == 200

def test_get_menu():
    api_client = APIClient()
    response = api_client.get_menu()
    assert response.status_code == 200

def test_publish_error():
    api_client = APIClient()
    error_code = "404"
    response = api_client.publish_error(error_code)
    assert response.status_code == 200
