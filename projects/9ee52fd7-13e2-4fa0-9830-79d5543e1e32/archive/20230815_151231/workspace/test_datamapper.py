import pytest
from datamapper import DataMapper

def test_map_data():
    mapper = DataMapper()
    get_menu_response = {"categories": {"test-category-id": {"id": "test-category-id", "name": "test-category-name"}}}
    mapping_json = {"categories.{{categoryId}}": {"input": {"path": "categories.{{categoryId}}"}, "output": {"path": "categories.{{categoryId}}"}}}
    result = mapper.map_data(get_menu_response, mapping_json)
    assert result == {"categories": {"test-category-id": {"id": "test-category-id", "name": "test-category-name"}}}
