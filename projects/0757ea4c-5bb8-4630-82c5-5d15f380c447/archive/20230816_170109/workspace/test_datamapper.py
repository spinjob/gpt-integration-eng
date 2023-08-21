import pytest
from datamapper import DataMapper

def test_map_data():
    mapper = DataMapper()
    data = {'key': 'value'}
    mapping = {'key': 'new_key'}
    result = mapper.map_data(data, mapping)
    assert result == {'new_key': 'value'}
