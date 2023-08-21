from requests_oauthlib import OAuth2Session

class OAuth2Authenticator:
    def __init__(self):
        # Initialize the OAuth2 session
        self.oauth = OAuth2Session("client-id", redirect_uri="redirect-uri")

    def get_access_token(self):
        # Get the access token
        token = self.oauth.fetch_token("token-url", client_secret="client-secret")
        return token["access_token"]

    def refresh_access_token(self, old_token):
        # Refresh the access token
        new_token = self.oauth.refresh_token("refresh-url", old_token)
        return new_token["access_token"]
