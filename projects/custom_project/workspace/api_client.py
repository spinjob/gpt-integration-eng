import requests

class APIClient:
    def __init__(self, url):
        self.url = url

    def get_data(self):
        response = requests.get(self.url)
        response.raise_for_status()
        return response.json()
