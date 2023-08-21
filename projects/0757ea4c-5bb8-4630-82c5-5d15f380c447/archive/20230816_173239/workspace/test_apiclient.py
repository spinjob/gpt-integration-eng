import pytest
from apiclient import APIClient

def test_get_request():
    client = APIClient()
    response = client.get('https://partners.cloudkitchens.com/test-endpoint')
    assert response.status_code == 200

def test_post_request():
    client = APIClient()
    response = client.post('https://partners.cloudkitchens.com/test-endpoint', {'key': 'value'})
    assert response.status_code == 200

def test_authentication():
    client = APIClient()
    token = client.get_token()
    assert token is not None
