import requests

class APIHandler:
    def __init__(self, url="https://api.example.com/data"):
        self.url = url

    def fetch_data(self):
        response = requests.get(self.url)
        response.raise_for_status()
        return response.json()
