import requests

class APIClient:
    def __init__(self):
        self.base_url = 'https://partners.cloudkitchens.com'

    def request(self, endpoint, data):
        response = requests.post(self.base_url + endpoint, json=data)
        return response.json()
