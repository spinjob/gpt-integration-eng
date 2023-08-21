from webhookhandler import WebhookHandler
from apirequester import APIRequester
from datamapper import DataMapper
from oauth2authenticator import OAuth2Authenticator

class WorkflowManager:
    def __init__(self):
        self.webhook_handler = WebhookHandler()
        self.api_requester = APIRequester()
        self.data_mapper = DataMapper()
        self.authenticator = OAuth2Authenticator()

    def start_workflow(self, webhook_body):
        # Handle the webhook
        store_id = self.webhook_handler.handle_webhook(webhook_body)

        # Get the access token
        access_token = self.authenticator.get_access_token()

        # Make the getMenu request
        get_menu_response = self.api_requester.get_request("https://partners.cloudkitchens.com/getMenu", {"X-Store-Id": store_id}, access_token)

        # Map the data for the upsertMenu request
        mapping_json = {"categories.{{categoryId}}": {"input": {"path": "categories.{{categoryId}}"}, "output": {"path": "categories.{{categoryId}}"}}}
        upsert_menu_body = self.data_mapper.map_data(get_menu_response, mapping_json)

        # Make the upsertMenu request
        upsert_menu_response = self.api_requester.post_request("https://partners.cloudkitchens.com/upsertMenu", upsert_menu_body, access_token)

        return True
