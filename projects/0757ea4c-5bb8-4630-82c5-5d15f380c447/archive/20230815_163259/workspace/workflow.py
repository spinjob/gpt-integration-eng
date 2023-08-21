from api import API
from auth import Auth
from data_mapping import DataMapping

class Workflow:
    def __init__(self):
        self.pos_api = API('https://partners.cloudkitchens.com', Auth('/v1/auth/token', 'pos_client_id', 'pos_client_secret', 'menus.get_current menus.publish orders.update storefront.store_availability menus.entity_suspension orders.create'))
        self.marketplace_api = API('https://partners.cloudkitchens.com', Auth('/v1/auth/token', 'marketplace_client_id', 'marketplace_client_secret', 'callback.error.write manager.menus manager.orders menus.async_job.read menus.get_current menus.read menus.upsert menus.upsert_hours orders.read ping'))

    def execute(self, trigger_data):
        data_mapping = DataMapping(trigger_data)
        # Execute the workflow steps as per the instructions
