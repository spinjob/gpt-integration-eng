import pytest
from formulas import if_then, substring, prepend, division

def test_if_then():
    assert if_then("USD", "equals", "USD", "United States Dollar", "USD") == "United States Dollar"

def test_substring():
    assert substring("123456", 0, 4) == "1234"

def test_prepend():
    assert prepend("1234", "ID: ") == "ID: 1234"

def test_division():
    assert division(100, 10) == 10
