from api_client import APIClient
from auth import OAuth2ClientCredentials
from data_mapper import DataMapper

class Workflow:
    def __init__(self):
        self.marketplace_api = APIClient(
            'https://partners.cloudkitchens.com',
            OAuth2ClientCredentials(
                'https://partners.cloudkitchens.com/v1/auth/token',
                'be04e745-844d-4a6c-8fba-f71199dc8f05',
                'MD727PM35KZCWP337TKQ',
                'callback.error.write manager.menus manager.orders menus.async_job.read menus.get_current menus.read menus.upsert menus.upsert_hours orders.read ping'
            )
        )
        self.pos_api = APIClient(
            'https://partners.cloudkitchens.com',
            OAuth2ClientCredentials(
                'https://partners.cloudkitchens.com/v1/auth/token',
                '04db98cc-0c84-47e2-b57f-bfd6329c4675',
                'NUCGB6VKFLYQBZPMMBLA',
                'menus.get_current menus.publish orders.update storefront.store_availability menus.entity_suspension orders.create'
            )
        )
        self.data_mapper = DataMapper()

    def execute(self, trigger_data):
        # Step 1: Create order
        data_mapping = self.data_mapper.map(trigger_data, step1_data_mapping_json)
        response = self.pos_api.request('POST', '/orders', json=data_mapping)
        # Step 2: Update order status
        data_mapping = self.data_mapper.map(response, step2_data_mapping_json)
        self.marketplace_api.request('PUT', f'/orders/{data_mapping["orderId"]}', json=data_mapping)
        # Step 3: Get menu
        data_mapping = self.data_mapper.map(response, step3_data_mapping_json)
        self.pos_api.request('GET', '/menu', headers=data_mapping)
        # Step 4: Publish error
        data_mapping = self.data_mapper.map(response, step4_data_mapping_json)
        self.marketplace_api.request('POST', '/errors', headers=data_mapping)
