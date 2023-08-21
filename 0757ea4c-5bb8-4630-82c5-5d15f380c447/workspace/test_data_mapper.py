import pytest
from data_mapper import DataMapper

def test_extract_data():
    mapper = DataMapper()
    data = {"key": "value"}
    assert mapper.extract_data(data, "key") == "value"

def test_apply_formula():
    mapper = DataMapper()
    assert mapper.apply_formula("value", "formula") == "value"

def test_set_output():
    mapper = DataMapper()
    data = {"key": "value"}
    mapper.set_output(data, "key", "new_value")
    assert data["key"] == "new_value"
