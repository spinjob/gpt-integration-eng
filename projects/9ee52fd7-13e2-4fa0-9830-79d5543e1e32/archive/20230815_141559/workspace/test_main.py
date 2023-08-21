import pytest
from main import main

def test_main():
    request = {"body": {"metadata": {"storeId": "123"}}}
    response = main(request)
    assert isinstance(response, dict)
