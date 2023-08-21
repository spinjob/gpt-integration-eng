import requests
from auth import OAuth2

class APIClient:
    def __init__(self):
        self.auth = OAuth2()

    def create_order(self, data):
        url = 'https://partners.cloudkitchens.com/v1/orders'
        headers = {'Authorization': 'Bearer ' + self.auth.get_token()}
        response = requests.post(url, headers=headers, json=data)
        return response.json()

    def update_order_status(self, data):
        url = 'https://partners.cloudkitchens.com/v1/orders/' + data['orderId']
        headers = {'Authorization': 'Bearer ' + self.auth.get_token()}
        response = requests.put(url, headers=headers, json=data)
        return response.json()

    def get_menu(self, data):
        url = 'https://partners.cloudkitchens.com/v1/menus/' + data['menuId']
        headers = {'Authorization': 'Bearer ' + self.auth.get_token()}
        response = requests.get(url, headers=headers)
        return response.json()

    def publish_error(self, data):
        url = 'https://partners.cloudkitchens.com/v1/errors'
        headers = {'Authorization': 'Bearer ' + self.auth.get_token()}
        response = requests.post(url, headers=headers, json=data)
        return response.json()
