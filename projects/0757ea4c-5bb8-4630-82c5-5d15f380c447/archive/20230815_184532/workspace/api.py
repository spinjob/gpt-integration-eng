import requests
from dotenv import load_dotenv
import os

load_dotenv()

class API:
    def __init__(self, api_id):
        self.api_id = api_id
        self.base_url = os.getenv(f'{api_id.upper()}_API_BASE_URL')
        self.client_id = os.getenv(f'{api_id.upper()}_API_CLIENT_ID')
        self.client_secret = os.getenv(f'{api_id.upper()}_API_CLIENT_SECRET')
        self.token = self.get_token()

    def get_token(self):
        url = f'{self.base_url}/v1/auth/token'
        data = {
            'client_id': self.client_id,
            'client_secret': self.client_secret,
            'scope': 'callback.error.write manager.menus manager.orders menus.async_job.read menus.get_current menus.read menus.upsert menus.upsert_hours orders.read ping',
            'grant_type': 'client_credentials'
        }
        response = requests.post(url, data=data)
        response.raise_for_status()
        return response.json()['access_token']

    def make_request(self, method, path, headers=None, params=None, data=None):
        url = f'{self.base_url}{path}'
        headers = headers or {}
        headers['Authorization'] = f'Bearer {self.token}'
        response = requests.request(method, url, headers=headers, params=params, json=data)
        response.raise_for_status()
        return response.json()
