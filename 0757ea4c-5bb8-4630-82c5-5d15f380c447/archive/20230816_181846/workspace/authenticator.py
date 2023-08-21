import requests

class Authenticator:
    def __init__(self):
        self.token_url = "https://partners.cloudkitchens.com/v1/auth/token"
        self.marketplace_api_credentials = {
            "client_id": "be04e745-844d-4a6c-8fba-f71199dc8f05",
            "client_secret": "MD727PM35KZCWP337TKQ",
            "scope": "callback.error.write manager.menus manager.orders menus.async_job.read menus.get_current menus.read menus.upsert menus.upsert_hours orders.read ping",
            "grant_type": "client_credentials"
        }
        self.point_of_sale_api_credentials = {
            "client_id": "04db98cc-0c84-47e2-b57f-bfd6329c4675",
            "client_secret": "NUCGB6VKFLYQBZPMMBLA",
            "scope": "menus.get_current menus.publish orders.update storefront.store_availability menus.entity_suspension orders.create",
            "grant_type": "client_credentials"
        }

    def authenticate(self):
        # Authenticate with the Marketplace API
        self.marketplace_api_token = self.get_token(self.marketplace_api_credentials)

        # Authenticate with the Point-of-Sale API
        self.point_of_sale_api_token = self.get_token(self.point_of_sale_api_credentials)

    def get_token(self, credentials):
        # Get an access token
        response = requests.post(self.token_url, data=credentials)
        response.raise_for_status()
        return response.json()["access_token"]
