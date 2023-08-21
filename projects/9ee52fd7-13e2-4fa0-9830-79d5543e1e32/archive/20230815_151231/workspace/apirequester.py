import requests

class APIRequester:
    def get_request(self, url, headers, access_token):
        # Add the access token to the headers
        headers["Authorization"] = f"Bearer {access_token}"

        # Make the GET request
        response = requests.get(url, headers=headers)
        return response.json()

    def post_request(self, url, body, access_token):
        # Add the access token to the headers
        headers = {"Authorization": f"Bearer {access_token}"}

        # Make the POST request
        response = requests.post(url, json=body, headers=headers)
        return response.json()
