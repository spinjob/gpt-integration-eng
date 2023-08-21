import requests

class OAuth2Client:
    def __init__(self, client_id, client_secret, token_url):
        self.client_id = client_id
        self.client_secret = client_secret
        self.token_url = token_url
        self.token = None

    def generate_token(self):
        data = {
            'client_id': self.client_id,
            'client_secret': self.client_secret,
            'grant_type': 'client_credentials'
        }
        response = requests.post(self.token_url, data=data)
        response.raise_for_status()
        self.token = response.json()['access_token']
        return self.token

    def refresh_token(self):
        self.generate_token()
