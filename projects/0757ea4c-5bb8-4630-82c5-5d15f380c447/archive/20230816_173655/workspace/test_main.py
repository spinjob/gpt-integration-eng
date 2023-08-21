import pytest
from main import main

def test_main():
    result = main()
    assert result is not None
