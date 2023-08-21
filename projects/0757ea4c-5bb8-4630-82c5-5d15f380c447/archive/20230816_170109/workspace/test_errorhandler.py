import pytest
from errorhandler import ErrorHandler

def test_handle_error():
    handler = ErrorHandler()
    error = 'Test error'
    result = handler.handle_error(error)
    assert result == 'Error handled'
