from api_client import APIClient
from data_processor import DataProcessor

def main():
    client = APIClient('https://api.example.com')
    data = client.fetch_data('endpoint')

    processor = DataProcessor()
    processed_data = processor.process_data(data)

    print(processed_data)

if __name__ == "__main__":
    main()
