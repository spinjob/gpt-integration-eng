import pytest
from main import main

def test_main():
    output = main()
    assert output is True
