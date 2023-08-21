import pytest
from datamapper import DataMapper

def test_extract_value():
    mapper = DataMapper()
    value = mapper.extract_value({'key': 'value'}, 'key')
    assert value == 'value'

def test_apply_formula():
    mapper = DataMapper()
    value = mapper.apply_formula('value', lambda x: x.upper())
    assert value == 'VALUE'

def test_set_value():
    mapper = DataMapper()
    output = {}
    mapper.set_value(output, 'key', 'value')
    assert output['key'] == 'value'
