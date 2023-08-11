from api_client import APIClient
from data_processor import process_data

def main():
    client = APIClient()
    data = client.fetch_data()
    processed_data = process_data(data)
    print(processed_data)

if __name__ == "__main__":
    main()
