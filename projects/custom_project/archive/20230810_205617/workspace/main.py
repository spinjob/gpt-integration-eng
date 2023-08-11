from api_client import APIClient
from data_processor import DataProcessor

def main():
    # Create an instance of APIClient
    api_client = APIClient()

    # Fetch data from the API
    data = api_client.fetch_data()

    # Create an instance of DataProcessor
    data_processor = DataProcessor()

    # Process the data
    processed_data = data_processor.process_data(data)

    # Print the processed data
    print(processed_data)

if __name__ == "__main__":
    main()
