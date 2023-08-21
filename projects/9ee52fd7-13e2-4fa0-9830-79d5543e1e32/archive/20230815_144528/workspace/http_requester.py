import requests
from oauth2_authenticator import OAuth2Authenticator

class HttpRequester:
    def __init__(self):
        self.authenticator = OAuth2Authenticator()

    def send_request(self, api_id, method, path, headers, body):
        # Authenticate with the API
        access_token = self.authenticator.authenticate(api_id)
        headers['Authorization'] = f'Bearer {access_token}'

        # Send the HTTP request
        url = f'https://partners.cloudkitchens.com{path}'
        response = requests.request(method, url, headers=headers, json=body)

        # Return the response body as a dictionary
        return response.json()
