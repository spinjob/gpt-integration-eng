from api_client import APIClient

class OAuth2Client(APIClient):
    def __init__(self, base_url, token_url, client_id, client_secret, scope):
        super().__init__(base_url)
        self.token_url = token_url
        self.client_id = client_id
        self.client_secret = client_secret
        self.scope = scope
        self.token = None

    def authenticate(self):
        data = {
            'client_id': self.client_id,
            'client_secret': self.client_secret,
            'scope': self.scope,
            'grant_type': 'client_credentials'
        }
        response = self.post(self.token_url, data=data)
        response.raise_for_status()
        self.token = response.json()['access_token']

    def get(self, path, headers=None, params=None):
        if self.token is None:
            self.authenticate()
        if headers is None:
            headers = {}
        headers['Authorization'] = f'Bearer {self.token}'
        return super().get(path, headers=headers, params=params)

    def post(self, path, headers=None, data=None):
        if self.token is None:
            self.authenticate()
        if headers is None:
            headers = {}
        headers['Authorization'] = f'Bearer {self.token}'
        return super().post(path, headers=headers, data=data)
