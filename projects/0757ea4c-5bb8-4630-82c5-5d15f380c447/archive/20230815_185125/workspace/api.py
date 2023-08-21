import requests

class API:
    def __init__(self, base_url, auth):
        self.base_url = base_url
        self.auth = auth

    def send_request(self, method, endpoint, headers=None, params=None, data=None):
        # Get the access token
        access_token = self.auth.get_access_token()

        # Add the access token to the headers
        if headers is None:
            headers = {}
        headers['Authorization'] = f'Bearer {access_token}'

        # Send the request
        response = requests.request(method, self.base_url + endpoint, headers=headers, params=params, json=data)

        # Return the response
        return response.json()
