import requests
from requests.auth import HTTPBasicAuth

class APIHandler:
    def __init__(self):
        self.session = requests.Session()
        self.session.auth = HTTPBasicAuth('username', 'password')  # Replace with actual username and password

    def send_get_request(self, url, api_id):
        headers = {'X-API-ID': api_id}
        response = self.session.get(url, headers=headers)
        response.raise_for_status()
        return response

    def send_post_request(self, url, api_id, data):
        headers = {'X-API-ID': api_id, 'Content-Type': 'application/json'}
        response = self.session.post(url, headers=headers, data=json.dumps(data))
        response.raise_for_status()
        return response
