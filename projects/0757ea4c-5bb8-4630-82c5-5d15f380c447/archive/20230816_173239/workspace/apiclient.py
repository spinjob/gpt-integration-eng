import requests

class APIClient:
    def post(self, url, data):
        response = requests.post(url, json=data)
        response.raise_for_status()
        return response.json()

    def get(self, url, params):
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()
