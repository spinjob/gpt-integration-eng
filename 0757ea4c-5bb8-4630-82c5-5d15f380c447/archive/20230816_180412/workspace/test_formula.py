import pytest
from formula import Formula

def test_apply():
    formula = Formula()
    result = formula.apply("input")
    assert result == "output"
