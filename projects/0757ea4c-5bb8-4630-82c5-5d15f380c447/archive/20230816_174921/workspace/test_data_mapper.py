import pytest
from data_mapper import DataMapper

def test_find_input_data():
    mapper = DataMapper()
    input_data = mapper.find_input_data('test', {'test': 'data'})
    assert input_data == 'data'

def test_apply_formula():
    mapper = DataMapper()
    output_data = mapper.apply_formula('uppercase', 'test')
    assert output_data == 'TEST'

def test_set_output_value():
    mapper = DataMapper()
    output_data = mapper.set_output_value('test', {'test': 'data'})
    assert output_data == 'data'
