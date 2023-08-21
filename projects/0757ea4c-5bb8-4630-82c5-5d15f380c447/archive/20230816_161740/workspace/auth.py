import requests

class OAuth2ClientCredentials:
    def __init__(self, token_url, client_id, client_secret, scope):
        self.token_url = token_url
        self.client_id = client_id
        self.client_secret = client_secret
        self.scope = scope
        self.token = None

    def get_token(self):
        if not self.token:
            data = {
                'client_id': self.client_id,
                'client_secret': self.client_secret,
                'scope': self.scope,
                'grant_type': 'client_credentials'
            }
            response = requests.post(self.token_url, data=data)
            response.raise_for_status()
            self.token = response.json()['access_token']
        return self.token
