import requests

class APIClient:
    def __init__(self):
        self.base_url = "https://partners.cloudkitchens.com"

    def make_request(self, method, path, headers=None, params=None, data=None):
        # Make an HTTP request
        url = self.base_url + path
        response = requests.request(method, url, headers=headers, params=params, data=data)
        response.raise_for_status()
        return response.json()
