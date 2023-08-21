import pytest
from data_mapper import DataMapper

def test_data_mapper_init():
    mapper = DataMapper()
    assert mapper is not None

def test_data_mapper_map_data():
    mapper = DataMapper()
    mapping_instructions = {"test": "instructions"}
    data = {"test": "data"}
    assert mapper.map_data(mapping_instructions, data) == True
