import pytest
from datamapper import DataMapper

def test_data_mapping():
    mapper = DataMapper()
    output = mapper.map_data({'key': 'value'}, {'key': 'output_key'})
    assert output == {'output_key': 'value'}
