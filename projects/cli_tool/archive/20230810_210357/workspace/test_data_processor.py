from data_processor import process_data

def test_process_data():
    data = {"test": "data"}
    processed_data = process_data(data)
    assert processed_data == data
