import pytest
from errorhandler import ErrorHandler

def test_error_handling():
    handler = ErrorHandler()
    response = handler.handle_error(Exception('Test error'))
    assert response.status_code == 200
