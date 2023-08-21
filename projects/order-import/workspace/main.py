from api_client import APIClient
from token_generator import TokenGenerator
from data_transformer import DataTransformer

def main():
    # Generate bearer tokens for both APIs
    token_generator = TokenGenerator()
    token1 = token_generator.generate_token(api_number=1)
    token2 = token_generator.generate_token(api_number=2)

    # Make a GET request to API #1
    api_client = APIClient()
    response = api_client.get(api_number=1, path='/v1/menu', headers={'X-Store-Id': 'store_id', 'Authorization': f'Bearer {token1}'})

    # Transform the data received from API #1
    data_transformer = DataTransformer()
    transformed_data = data_transformer.transform(response)

    # Make a POST request to API #2 with the transformed data
    api_client.post(api_number=2, path='/v1/menus', headers={'X-Store-Id': 'store_id', 'Authorization': f'Bearer {token2}'}, data=transformed_data)

if __name__ == '__main__':
    main()
