import pytest
from data_mapper import DataMapper

def test_map_data():
    mapper = DataMapper()
    mapping_json = {
        "X-Store-Id": {
            "input": {"in": "body", "sourcePath": "metadata.storeId"},
            "output": {"in": "header", "outputPath": "X-Store-Id"}
        }
    }
    source_data = {"metadata": {"storeId": "test-store-id"}}
    mapped_data = mapper.map_data(mapping_json, source_data)
    assert mapped_data == {"X-Store-Id": "test-store-id"}
