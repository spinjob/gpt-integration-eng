from api_handler import APIHandler
from database_handler import DatabaseHandler
from data_processor import DataProcessor

def main():
    api_handler = APIHandler()
    data_processor = DataProcessor()
    database_handler = DatabaseHandler()

    raw_data = api_handler.fetch_data()
    processed_data = data_processor.process_data(raw_data)
    database_handler.store_data(processed_data)

if __name__ == "__main__":
    main()
