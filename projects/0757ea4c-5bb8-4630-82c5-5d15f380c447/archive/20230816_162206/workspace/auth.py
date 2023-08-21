import requests

def get_token(api_name):
    url = 'https://partners.cloudkitchens.com/v1/auth/token'
    data = {
        'client_id': 'client_id_value',
        'client_secret': 'client_secret_value',
        'scope': 'scope_value',
        'grant_type': 'client_credentials'
    }
    response = requests.post(url, data=data)
    response.raise_for_status()
    return response.json()['access_token']
