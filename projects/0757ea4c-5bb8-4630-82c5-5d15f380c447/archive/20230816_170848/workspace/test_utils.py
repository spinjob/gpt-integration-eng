import pytest
from utils import apply_formula

def test_apply_formula():
    result = apply_formula('test_input_value', 'test_formula')
    assert result is not None
