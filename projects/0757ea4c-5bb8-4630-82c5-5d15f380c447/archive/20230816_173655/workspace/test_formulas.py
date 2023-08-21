import pytest
from formulas import ifthen, substring, prepend, division

def test_ifthen():
    result = ifthen('test', 'equals', 'test', 'yes', 'no')
    assert result == 'yes'

def test_substring():
    result = substring('test_string', 0, 4)
    assert result == 'test'

def test_prepend():
    result = prepend('test', 'prefix_')
    assert result == 'prefix_test'

def test_division():
    result = division(10, 2)
    assert result == 5
