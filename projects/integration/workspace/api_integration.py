import requests
from translator import Translator

class APIIntegration:
    def __init__(self):
        self.translator = Translator()

    def run(self):
        # Generate bearer tokens for both APIs
        token1 = self.get_token('https://partners.cloudkitchens.com/v1/auth/token', 'client_credentials', 'clientId1', 'clientSecret1', 'menus.get_current menus.publish orders.update storefront.store_availability menus.entity_suspension orders.create')
        token2 = self.get_token('https://partners.cloudkitchens.com/v1/auth/token', 'client_credentials', 'clientId2', 'clientSecret2', 'callback.error.write manager.menus manager.orders menus.async_job.read menus.get_current menus.read menus.upsert menus.upsert_hours orders.read ping')

        # Make a GET request to API #1
        response = requests.get('https://partners.cloudkitchens.com/v1/menu', headers={'X-Store-Id': 'storeId', 'Authorization': f'Bearer {token1}'})

        # Translate the response into a new JSON object
        translated_data = self.translator.translate(response.json())

        # Make a POST request to API #2
        requests.post('https://partners.cloudkitchens.com/v1/menus', headers={'X-Store-Id': 'storeId', 'Authorization': f'Bearer {token2}'}, json=translated_data)

    def get_token(self, url, grant_type, client_id, client_secret, scope):
        # Make a POST request to get the token
        response = requests.post(url, data={'grant_type': grant_type, 'client_id': client_id, 'client_secret': client_secret, 'scope': scope})

        # Return the token
        return response.json()['access_token']
