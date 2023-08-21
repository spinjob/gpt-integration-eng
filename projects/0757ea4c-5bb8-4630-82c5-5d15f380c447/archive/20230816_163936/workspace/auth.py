import requests

class OAuth2ClientCredentials:
    def __init__(self):
        self.tokens = {}

    def get_token(self, api_name):
        if api_name not in self.tokens:
            self.tokens[api_name] = self._request_token(api_name)
        return self.tokens[api_name]

    def _request_token(self, api_name):
        url = 'https://partners.cloudkitchens.com/v1/auth/token'
        data = {
            'client_id': 'client_id_for_' + api_name,
            'client_secret': 'client_secret_for_' + api_name,
            'scope': 'scope_for_' + api_name,
            'grant_type': 'client_credentials'
        }
        response = requests.post(url, data=data)
        response.raise_for_status()
        return response.json()['access_token']
