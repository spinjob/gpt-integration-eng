import pytest
from error_handler import ErrorHandler

def test_handle_error():
    handler = ErrorHandler()
    exception = Exception("Test error")
    message = handler.handle_error(exception)
    assert message == "Test error"
