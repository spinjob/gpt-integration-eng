import requests

class APIClient:
    def __init__(self, base_url, client_id, client_secret, scope, grant_type):
        self.base_url = base_url
        self.client_id = client_id
        self.client_secret = client_secret
        self.scope = scope
        self.grant_type = grant_type
        self.token = self._get_token()

    def _get_token(self):
        url = f"{self.base_url}/v1/auth/token"
        data = {
            "client_id": self.client_id,
            "client_secret": self.client_secret,
            "scope": self.scope,
            "grant_type": self.grant_type
        }
        response = requests.post(url, data=data)
        response.raise_for_status()
        return response.json()["access_token"]

    def get(self, path, headers=None):
        url = f"{self.base_url}{path}"
        headers = headers or {}
        headers["Authorization"] = f"Bearer {self.token}"
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()

    def post(self, path, data, headers=None):
        url = f"{self.base_url}{path}"
        headers = headers or {}
        headers["Authorization"] = f"Bearer {self.token}"
        response = requests.post(url, json=data, headers=headers)
        response.raise_for_status()
        return response.json()
