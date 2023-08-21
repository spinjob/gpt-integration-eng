import pytest
from main import main

def test_main():
    response = main()
    assert isinstance(response, dict)
