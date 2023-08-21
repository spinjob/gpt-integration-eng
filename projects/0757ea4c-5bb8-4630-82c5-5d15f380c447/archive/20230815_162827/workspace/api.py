import requests

class API:
    def __init__(self):
        self.session = requests.Session()

    def request(self, method, url, headers=None, params=None, data=None):
        response = self.session.request(method, url, headers=headers, params=params, data=data)
        response.raise_for_status()
        return response.json()
