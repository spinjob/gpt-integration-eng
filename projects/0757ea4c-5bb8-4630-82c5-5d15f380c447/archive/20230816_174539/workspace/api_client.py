import requests

class APIClient:
    def request(self, method, url, headers=None, data=None):
        # Send a request to the API and return the response
        response = requests.request(method, url, headers=headers, data=data)
        return response.json()
