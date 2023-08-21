import pytest
from data_mapping import DataMapping

def test_map_data():
    mapping = DataMapping()
    data = {'test': 'data'}
    mapped_data = mapping.map_data(data=data)
    assert isinstance(mapped_data, dict)
