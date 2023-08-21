from apiclient import APIClient

class OAuth2ClientCredentials:
    def __init__(self, client_id, client_secret, token_url):
        self.client_id = client_id
        self.client_secret = client_secret
        self.token_url = token_url
        self.api_client = APIClient('')

    def generate_token(self):
        data = {
            'client_id': self.client_id,
            'client_secret': self.client_secret,
            'grant_type': 'client_credentials'
        }
        response = self.api_client.post(self.token_url, data=data)
        return response.json()['access_token']
