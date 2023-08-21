import requests

class OAuth2Authenticator:
    def __init__(self):
        self.client_id = 'your_client_id'
        self.client_secret = 'your_client_secret'
        self.token_url = 'https://partners.cloudkitchens.com/oauth/token'

    def authenticate(self, api_id):
        data = {
            'grant_type': 'client_credentials',
            'client_id': self.client_id,
            'client_secret': self.client_secret,
            'audience': api_id
        }
        response = requests.post(self.token_url, data=data)
        response.raise_for_status()  # Raise exception if the request failed
        return response.json()['access_token']
