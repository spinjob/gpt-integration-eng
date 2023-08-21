import pytest
from formulas import if_then, substring, prepend, division

def test_if_then():
    output = if_then('value', 'value', 'output1', 'output2')
    assert output == 'output1'

def test_substring():
    output = substring('value', 1, 3)
    assert output == 'alu'

def test_prepend():
    output = prepend('value', 'pre')
    assert output == 'prevalue'

def test_division():
    output = division(10, 2)
    assert output == 5
