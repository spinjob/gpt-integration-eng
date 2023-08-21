import json
from api_handler import APIHandler
from data_mapper import DataMapper

def main():
    # Initialize APIHandler and DataMapper
    api_handler = APIHandler()
    data_mapper = DataMapper()

    # Step 1: Get menu from Marketplace API
    response = api_handler.send_get_request('https://partners.cloudkitchens.com/getMenu', '2389bc50-2646-4e94-bb34-86c9ea23cd7e')
    menu_data = json.loads(response.text)

    # Step 2: Map the data for the Point-of-Sale API
    mapped_data = data_mapper.map_data(menu_data)

    # Step 3: Upsert menu to Point-of-Sale API
    api_handler.send_post_request('https://partners.cloudkitchens.com/upsertMenu', '98ef9a91-f0ca-4e0a-acd3-4618904fd6b4', mapped_data)

if __name__ == "__main__":
    main()
