import requests

class TokenGenerator:
    TOKEN_URLS = {
        1: 'https://partners.cloudkitchens.com/v1/auth/token',
        2: 'https://partners.cloudkitchens.com/v1/auth/token'
    }

    def generate_token(self, api_number):
        url = self.TOKEN_URLS[api_number]
        data = {
            'scope': 'menus.get_current menus.publish orders.update storefront.store_availability menus.entity_suspension orders.create' if api_number == 1 else 'callback.error.write manager.menus manager.orders menus.async_job.read menus.get_current menus.read menus.upsert menus.upsert_hours orders.read ping',
            'grant_type': 'client_credentials',
            'client_id': 'client_id',
            'client_secret': 'client_secret'
        }
        response = requests.post(url, data=data)
        response.raise_for_status()
        return response.json()['access_token']
