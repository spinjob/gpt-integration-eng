import requests

class OAuth2Authenticator:
    def authenticate(self, credentials):
        # Perform OAuth2 authentication and return access token
        response = requests.post('https://oauth2-server.com/token', data=credentials)
        token = response.json()['access_token']
        return token
