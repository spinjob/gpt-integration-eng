import requests

class APIClient:
    def __init__(self, base_url):
        self.base_url = base_url

    def get(self, path, headers=None, params=None):
        return requests.get(self.base_url + path, headers=headers, params=params)

    def post(self, path, headers=None, data=None):
        return requests.post(self.base_url + path, headers=headers, data=data)
