import pytest
from error_handler import ErrorHandler

def test_error_handler():
    error_handler = ErrorHandler()
    assert error_handler.handle_error() is None
