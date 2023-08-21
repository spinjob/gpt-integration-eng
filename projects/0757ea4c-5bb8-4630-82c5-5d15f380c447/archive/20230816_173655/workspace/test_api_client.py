import pytest
from api_client import APIClient

def test_send_get_request():
    client = APIClient(base_url='https://test.com')
    response = client.send_get_request('/test_endpoint')
    assert response.status_code == 200

def test_send_post_request():
    client = APIClient(base_url='https://test.com')
    response = client.send_post_request('/test_endpoint', data={'test_key': 'test_value'})
    assert response.status_code == 200
