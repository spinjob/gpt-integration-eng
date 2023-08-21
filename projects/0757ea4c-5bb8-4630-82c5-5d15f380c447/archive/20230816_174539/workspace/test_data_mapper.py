import pytest
from data_mapper import DataMapper

def test_map_data():
    data_mapper = DataMapper()
    mapping_instructions = {"currencyCode": {"input": {"path": "metadata.payload.currencyCode"}}}
    webhook_data = {"metadata": {"payload": {"currencyCode": "USD"}}}
    mapped_data = data_mapper.map_data(mapping_instructions, webhook_data)
    assert mapped_data == {"currencyCode": "USD"}
