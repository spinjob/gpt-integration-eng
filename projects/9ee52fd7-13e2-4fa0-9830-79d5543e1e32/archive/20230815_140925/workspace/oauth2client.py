import requests
from requests_oauthlib import OAuth2Session

class OAuth2Client:
    def __init__(self, client_id, client_secret, token_url):
        self.client_id = client_id
        self.client_secret = client_secret
        self.token_url = token_url
        self.session = OAuth2Session(client_id)

    def get_access_token(self):
        token = self.session.fetch_token(token_url=self.token_url, client_id=self.client_id, client_secret=self.client_secret)
        return token

    def refresh_access_token(self):
        token = self.session.refresh_token(self.token_url)
        return token
