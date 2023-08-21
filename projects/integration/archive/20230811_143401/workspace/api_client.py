import requests

class APIClient:
    def get(self, url, token):
        headers = {'Authorization': f'Bearer {token}'}
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response

    def post(self, url, token, data):
        headers = {'Authorization': f'Bearer {token}'}
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        return response
