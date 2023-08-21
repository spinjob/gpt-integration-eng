import pytest
from main import main

def test_main():
    response = main()
    assert response.status_code == 200
