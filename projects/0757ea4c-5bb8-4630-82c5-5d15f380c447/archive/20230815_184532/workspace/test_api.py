import pytest
from api import API

def test_get_token():
    api = API('MARKETPLACE')
    assert 'access_token' in api.token

def test_make_request():
    api = API('MARKETPLACE')
    response = api.make_request('GET', '/ping')
    assert response['status'] == 'OK'
