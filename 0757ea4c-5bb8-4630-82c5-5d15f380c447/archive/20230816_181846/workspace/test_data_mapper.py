import pytest
from data_mapper import DataMapper

def test_data_mapper():
    data_mapper = DataMapper()
    assert data_mapper.map_data() is None
