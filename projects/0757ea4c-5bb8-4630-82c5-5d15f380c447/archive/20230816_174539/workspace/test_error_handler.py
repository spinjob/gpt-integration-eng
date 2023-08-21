import pytest
from error_handler import ErrorHandler

def test_handle_error():
    error_handler = ErrorHandler()
    error_code = "404"
    response = error_handler.handle_error(error_code)
    assert response == "Error published successfully"
