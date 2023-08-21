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
        data = {'client_id': 'be04e745-844d-4a6c-8fba-f71199dc8f05'} if api_name == 'Marketplace API' else {'client_id': '04db98cc-0c84-47e2-b57f-bfd6329c4675'}
        response = requests.post(url, data=data)
        response.raise_for_status()
        return response.json()['access_token']
