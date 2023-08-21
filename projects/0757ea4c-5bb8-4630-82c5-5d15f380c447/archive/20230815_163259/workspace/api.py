import requests
from auth import Auth

class API:
    def __init__(self, base_url, auth):
        self.base_url = base_url
        self.auth = auth

    def request(self, method, path, headers=None, params=None, data=None):
        url = self.base_url + path
        headers = headers or {}
        headers['Authorization'] = 'Bearer ' + self.auth.get_token()
        response = requests.request(method, url, headers=headers, params=params, json=data)
        response.raise_for_status()
        return response.json()
