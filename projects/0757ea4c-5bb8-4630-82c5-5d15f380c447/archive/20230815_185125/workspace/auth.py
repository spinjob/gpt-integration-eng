import requests

class Auth:
    def __init__(self, client_id, client_secret, scope):
        self.client_id = client_id
        self.client_secret = client_secret
        self.scope = scope
        self.token_url = 'https://partners.cloudkitchens.com/v1/auth/token'

    def get_access_token(self):
        # Prepare the data for the token request
        data = {
            'client_id': self.client_id,
            'client_secret': self.client_secret,
            'scope': self.scope,
            'grant_type': 'client_credentials'
        }

        # Send the token request
        response = requests.post(self.token_url, data=data)

        # Return the access token
        return response.json()['access_token']
