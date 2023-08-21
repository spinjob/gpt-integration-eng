import pytest
from error_handler import ErrorHandler

def test_log_error():
    handler = ErrorHandler()
    result = handler.log_error('test_error')
    assert result is not None

def test_publish_error():
    handler = ErrorHandler()
    result = handler.publish_error('test_error')
    assert result is not None
