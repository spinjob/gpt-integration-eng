import requests

class APIClient:
    def __init__(self, base_url):
        self.base_url = base_url

    def get(self, path, headers=None):
        return requests.get(self.base_url + path, headers=headers)

    def post(self, path, data=None, headers=None):
        return requests.post(self.base_url + path, data=data, headers=headers)
