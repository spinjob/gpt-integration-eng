import requests
from data_mapping import DataMapping

class APIIntegration:
    def __init__(self, pos_api_client, marketplace_api_client):
        self.pos_api_client = pos_api_client
        self.marketplace_api_client = marketplace_api_client
        self.data_mapping = DataMapping()

    def get_menu(self, store_id):
        if not self.marketplace_api_client.token:
            self.marketplace_api_client.generate_token()
        headers = {
            'Authorization': f'Bearer {self.marketplace_api_client.token}',
            'X-Store-Id': store_id
        }
        response = requests.get('https://partners.cloudkitchens.com/v1/menus', headers=headers)
        response.raise_for_status()
        return response.json()

    def upsert_menu(self, menu):
        if not self.pos_api_client.token:
            self.pos_api_client.generate_token()
        headers = {
            'Authorization': f'Bearer {self.pos_api_client.token}'
        }
        data = self.data_mapping.map_data(menu)
        response = requests.post('https://partners.cloudkitchens.com/v1/menus', headers=headers, json=data)
        response.raise_for_status()
        return response.json()
