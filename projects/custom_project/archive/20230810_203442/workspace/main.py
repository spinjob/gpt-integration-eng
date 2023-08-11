from api import Api
from model import Database
from controller import Controller

def main():
    # Create instances of Api, Database, and Controller
    api = Api()
    db = Database()
    controller = Controller()

    # Fetch data from API
    data = api.fetch_data()

    # Process data
    processed_data = controller.process_data(data)

    # Store data in database
    db.store_data(processed_data)

if __name__ == "__main__":
    main()
