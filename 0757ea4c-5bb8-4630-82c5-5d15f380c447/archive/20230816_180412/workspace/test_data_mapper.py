import pytest
from data_mapper import DataMapper

def test_map():
    mapper = DataMapper()
    input = {"order": {"id": "123", "status": "NEW"}}
    mapping = {"order.id": {"sourcePath": "order.id", "targetPath": "id"}}
    output = mapper.map(input, mapping)
    assert output == {"id": "123"}
