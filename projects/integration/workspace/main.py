import schedule
import time
from api_client import APIClient
from token_generator import TokenGenerator
from data_transformer import DataTransformer

def run_integration():
    # Generate bearer tokens
    token_generator = TokenGenerator()
    token1 = token_generator.generate_token('client_id1', 'client_secret1', 'scope1')
    token2 = token_generator.generate_token('client_id2', 'client_secret2', 'scope2')

    # Make a GET request to API #1
    api_client = APIClient()
    response = api_client.get('https://partners.cloudkitchens.com/v1/menu', token1)

    # Transform the data
    data_transformer = DataTransformer()
    transformed_data = data_transformer.transform(response.json())

    # Make a POST request to API #2
    api_client.post('https://partners.cloudkitchens.com/v1/menus', token2, transformed_data)

# Schedule the job to run weekly at 7:00 PM Eastern Standard Time on Monday, Thursday, and Saturday
schedule.every().monday.at("19:00").do(run_integration)
schedule.every().thursday.at("19:00").do(run_integration)
schedule.every().saturday.at("19:00").do(run_integration)

while True:
    schedule.run_pending()
    time.sleep(1)
