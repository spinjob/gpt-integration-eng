import api
import processor

def main():
    # Fetch data from API
    data = api.fetch_data()
    
    # Process the fetched data
    processed_data = processor.process_data(data)
    
    print(processed_data)

if __name__ == "__main__":
    main()
