import requests
from auth import get_token

class PointOfSaleAPI:
    def __init__(self):
        self.base_url = 'https://partners.cloudkitchens.com'
        self.token = get_token('Point-of-Sale')

    def create_order(self, data):
        url = f'{self.base_url}/createOrder'
        headers = {'Authorization': f'Bearer {self.token}'}
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        return response.json()

    def get_menu(self, data):
        url = f'{self.base_url}/getMenu'
        headers = {'Authorization': f'Bearer {self.token}'}
        response = requests.get(url, headers=headers, json=data)
        response.raise_for_status()
        return response.json()

class MarketplaceAPI:
    def __init__(self):
        self.base_url = 'https://partners.cloudkitchens.com'
        self.token = get_token('Marketplace')

    def update_order_status(self, data):
        url = f'{self.base_url}/updateOrderStatus'
        headers = {'Authorization': f'Bearer {self.token}'}
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        return response.json()

    def publish_error(self, data):
        url = f'{self.base_url}/publishError'
        headers = {'Authorization': f'Bearer {self.token}'}
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        return response.json()
