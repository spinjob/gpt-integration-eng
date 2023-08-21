import pytest
from data_mapper import DataMapper

def test_map_data():
    mapper = DataMapper()
    data = {"storeId": "123"}
    mapping = {"X-Store-Id": {"input": {"in": "body", "sourcePath": "storeId"}}}
    output = mapper.map_data(data, mapping)
    assert output == {"X-Store-Id": "123"}
