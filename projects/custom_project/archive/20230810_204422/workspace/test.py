import pytest
import api
import processor

def test_fetch_data():
    data = api.fetch_data()
    assert isinstance(data, list)

def test_process_data():
    data = [{'field': 'value'}]
    processed_data = processor.process_data(data)
    assert processed_data == ['value']
