import pytest
from errorhandler import ErrorHandler

def test_log_error():
    handler = ErrorHandler()
    handler.log_error('error_message')
    assert handler.error_log == ['error_message']

def test_retry_request():
    handler = ErrorHandler()
    response = handler.retry_request('GET', 'https://example.com')
    assert response.status_code == 200

def test_publish_error():
    handler = ErrorHandler()
    response = handler.publish_error('error_code')
    assert response.status_code == 200
