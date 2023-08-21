import pytest
from error_handler import ErrorHandler

def test_error_handler_init():
    handler = ErrorHandler()
    assert handler is not None

def test_error_handler_handle_error():
    handler = ErrorHandler()
    error = Exception("Test error")
    assert handler.handle_error(error) == True
