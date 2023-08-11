import requests

class APIClient:
    def __init__(self):
        self.base_url = "http://example.com/api"

    def fetch_data(self):
        response = requests.get(self.base_url)
        data = response.json()
        return data
