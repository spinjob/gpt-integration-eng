import requests

class TokenGenerator:
    def generate_token(self, client_id, client_secret, scope):
        data = {
            'grant_type': 'client_credentials',
            'client_id': client_id,
            'client_secret': client_secret,
            'scope': scope
        }
        response = requests.post('https://partners.cloudkitchens.com/v1/auth/token', data=data)
        response.raise_for_status()
        return response.json()['access_token']
