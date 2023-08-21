import requests
from webhook_handler import WebhookHandler
from api_client import APIClient
from data_mapper import DataMapper
from workflow_manager import WorkflowManager
from error_handler import ErrorHandler

def main(webhook_data):
    # Create instances of the classes
    webhook_handler = WebhookHandler()
    api_client = APIClient()
    data_mapper = DataMapper()
    workflow_manager = WorkflowManager(api_client, data_mapper)
    error_handler = ErrorHandler(api_client)

    try:
        # Parse the webhook data
        parsed_data = webhook_handler.parse_webhook(webhook_data)

        # Run the workflow
        workflow_manager.run_workflow(parsed_data)
        
        return "Workflow completed successfully"
    except Exception as e:
        # Handle any errors
        error_handler.handle_error(str(e))
        return "Error occurred: " + str(e)

if __name__ == "__main__":
    # Placeholder for the webhook data
    webhook_data = {}
    main(webhook_data)
