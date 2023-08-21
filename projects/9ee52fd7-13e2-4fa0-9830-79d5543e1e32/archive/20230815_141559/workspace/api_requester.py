import requests

class APIRequester:
    def request(self, method, url, headers, body):
        # Perform HTTP request and return response
        response = requests.request(method, url, headers=headers, json=body)
        return response.json()
