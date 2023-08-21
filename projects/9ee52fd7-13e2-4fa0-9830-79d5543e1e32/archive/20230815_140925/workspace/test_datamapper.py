import pytest
from datamapper import DataMapper

def test_map_data():
    mapper = DataMapper(mapping_json={'test': {'input': {'in': 'body', 'sourcePath': 'test'}, 'output': {'in': 'body', 'outputPath': 'test'}}})
    data = mapper.map_data({'test': 'test'}, 'body')
    assert data == {'test': 'test'}
