import requests

class OAuth2:
    def get_token(self):
        url = 'https://partners.cloudkitchens.com/v1/auth/token'
        data = {'client_id': '04db98cc-0c84-47e2-b57f-bfd6329c4675'}
        response = requests.post(url, data=data)
        return response.json()['access_token']
