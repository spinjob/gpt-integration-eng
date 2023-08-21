import requests
from auth import OAuth2ClientCredentials

class APIClient:
    def __init__(self):
        self.auth = OAuth2ClientCredentials()

    def create_order(self, data):
        headers = {'Authorization': f'Bearer {self.auth.get_token("Marketplace API")}'}
        response = requests.post('https://partners.cloudkitchens.com/v1/orders', headers=headers, json=data)
        response.raise_for_status()
        return response.json()

    def update_order_status(self, data):
        headers = {'Authorization': f'Bearer {self.auth.get_token("Point-of-Sale API")}'}
        response = requests.put(f'https://partners.cloudkitchens.com/v1/orders/{data["orderId"]}', headers=headers, json=data)
        response.raise_for_status()
        return response.json()

    def get_menu(self, data):
        headers = {'Authorization': f'Bearer {self.auth.get_token("Marketplace API")}'}
        response = requests.get('https://partners.cloudkitchens.com/v1/menu', headers=headers)
        response.raise_for_status()
        return response.json()

    def publish_error(self, data):
        headers = {'Authorization': f'Bearer {self.auth.get_token("Point-of-Sale API")}'}
        response = requests.post('https://partners.cloudkitchens.com/v1/errors', headers=headers, json=data)
        response.raise_for_status()
