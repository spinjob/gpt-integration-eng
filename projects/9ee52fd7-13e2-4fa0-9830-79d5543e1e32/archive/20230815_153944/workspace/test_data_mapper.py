import pytest
from data_mapper import DataMapper

def test_map_data():
    mapper = DataMapper()
    assert mapper.map_data({}, {}) == True, "Data mapping should be successful"
