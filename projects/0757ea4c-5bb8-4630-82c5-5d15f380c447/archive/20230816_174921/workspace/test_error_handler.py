import pytest
from error_handler import ErrorHandler

def test_handle_error():
    handler = ErrorHandler()
    response = handler.handle_error(Exception('test error'))
    assert response.status_code == 500
