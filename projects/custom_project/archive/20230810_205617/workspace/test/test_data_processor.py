from data_processor import DataProcessor

def test_process_data():
    data_processor = DataProcessor()
    data = [{"name": "John", "age": 30}, {"name": "Jane", "age": 25}]
    processed_data = data_processor.process_data(data)
    assert isinstance(processed_data, pd.DataFrame)
