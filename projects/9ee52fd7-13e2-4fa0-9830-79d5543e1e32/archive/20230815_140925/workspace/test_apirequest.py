import pytest
from apirequest import APIRequest

def test_get_request():
    request = APIRequest(url='https://example.com/api', headers={'Authorization': 'Bearer test'})
    response = request.get('/test')
    assert response.status_code == 200

def test_post_request():
    request = APIRequest(url='https://example.com/api', headers={'Authorization': 'Bearer test'})
    response = request.post('/test', data={'test': 'test'})
    assert response.status_code == 200
