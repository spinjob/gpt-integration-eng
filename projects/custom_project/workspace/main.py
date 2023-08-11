from api_client import APIClient
from data_processor import DataProcessor

def main():
    api_client = APIClient('http://example.com/api/data')
    data = api_client.get_data()

    data_processor = DataProcessor()
    processed_data = data_processor.process_data(data)

    print(processed_data)

if __name__ == '__main__':
    main()
