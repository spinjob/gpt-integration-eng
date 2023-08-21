import requests

class APIRequest:
    def __init__(self, url, headers):
        self.url = url
        self.headers = headers

    def get(self, path):
        response = requests.get(self.url + path, headers=self.headers)
        return response.json()

    def post(self, path, data):
        response = requests.post(self.url + path, headers=self.headers, json=data)
        return response.json()
