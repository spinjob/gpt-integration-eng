import requests

class Api:
    def __init__(self, url="https://api.example.com/data"):
        self.url = url

    def fetch_data(self):
        response = requests.get(self.url)
        return response.json()
