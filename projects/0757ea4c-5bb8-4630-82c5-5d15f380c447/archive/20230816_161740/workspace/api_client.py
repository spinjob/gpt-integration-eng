import requests

class APIClient:
    def __init__(self, base_url, auth):
        self.base_url = base_url
        self.auth = auth

    def request(self, method, path, headers=None, params=None, json=None):
        url = self.base_url + path
        headers = headers or {}
        headers['Authorization'] = f'Bearer {self.auth.get_token()}'
        response = requests.request(method, url, headers=headers, params=params, json=json)
        response.raise_for_status()
        return response.json()
