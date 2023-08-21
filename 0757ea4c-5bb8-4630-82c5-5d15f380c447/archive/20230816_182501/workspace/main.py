import requests
from webhook_receiver import WebhookReceiver
from api_client import APIClient
from data_mapper import DataMapper
from workflow_manager import WorkflowManager
from error_handler import ErrorHandler

def main():
    # Initialize all the classes
    webhook_receiver = WebhookReceiver()
    api_client = APIClient()
    data_mapper = DataMapper()
    workflow_manager = WorkflowManager(webhook_receiver, api_client, data_mapper)
    error_handler = ErrorHandler(api_client)

    # Start the webhook receiver
    webhook_receiver.start()

    # Run the workflow
    try:
        workflow_manager.run_workflow()
    except Exception as e:
        # Handle any errors
        error_handler.handle_error(e)

if __name__ == "__main__":
    main()
