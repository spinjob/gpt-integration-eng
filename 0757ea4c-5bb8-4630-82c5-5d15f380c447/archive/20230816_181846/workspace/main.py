import requests
from webhook_handler import WebhookHandler
from api_client import APIClient
from workflow import Workflow
from data_mapper import DataMapper
from authenticator import Authenticator
from error_handler import ErrorHandler

def main():
    # Initialize the classes
    webhook_handler = WebhookHandler()
    api_client = APIClient()
    workflow = Workflow(api_client)
    data_mapper = DataMapper()
    authenticator = Authenticator()
    error_handler = ErrorHandler(api_client)

    # Start the webhook handler
    webhook_handler.start()

    # Main loop
    while True:
        # Check for new webhooks
        webhook = webhook_handler.check_for_webhook()
        if webhook is not None:
            # Authenticate with the APIs
            authenticator.authenticate()

            # Perform the workflow
            try:
                workflow.perform_workflow(webhook, data_mapper)
            except Exception as e:
                # Handle any errors
                error_handler.handle_error(e)

if __name__ == "__main__":
    main()
