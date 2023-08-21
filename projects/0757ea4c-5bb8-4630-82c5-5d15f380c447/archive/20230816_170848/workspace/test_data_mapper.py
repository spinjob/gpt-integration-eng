import pytest
from data_mapper import DataMapper

def test_map_data():
    mapper = DataMapper()
    result = mapper.map_data('test_input_data', 'test_mapping_rules')
    assert result is not None
