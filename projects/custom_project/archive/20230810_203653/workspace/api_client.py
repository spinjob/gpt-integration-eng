import requests
import json

class APIClient:
    def __init__(self, url="https://api.example.com/data"):
        self.url = url

    def fetch_data(self):
        response = requests.get(self.url)
        data = json.loads(response.text)
        return data
