import requests

class APIClient:
    BASE_URLS = {
        1: 'https://partners.cloudkitchens.com',
        2: 'https://partners.cloudkitchens.com'
    }

    def get(self, api_number, path, headers):
        url = self.BASE_URLS[api_number] + path
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()

    def post(self, api_number, path, headers, data):
        url = self.BASE_URLS[api_number] + path
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
