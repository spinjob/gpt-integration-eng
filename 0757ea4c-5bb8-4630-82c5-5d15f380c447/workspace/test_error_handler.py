import pytest
from error_handler import ErrorHandler

def test_log_error():
    handler = ErrorHandler()
    assert handler.log_error("error") is None

def test_send_notification():
    handler = ErrorHandler()
    assert handler.send_notification("error") is None
