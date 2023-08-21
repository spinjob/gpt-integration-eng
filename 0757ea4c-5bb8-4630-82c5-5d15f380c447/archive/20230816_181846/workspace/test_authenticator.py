import pytest
from authenticator import Authenticator

def test_authenticator():
    authenticator = Authenticator()
    assert authenticator.authenticate() is None
