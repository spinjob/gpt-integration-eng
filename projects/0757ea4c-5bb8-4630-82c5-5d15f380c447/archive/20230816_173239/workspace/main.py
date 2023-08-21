from webhookhandler import WebhookHandler
from workflow import Workflow

def main():
    # Create instances of the WebhookHandler and Workflow classes
    webhook_handler = WebhookHandler()
    workflow = Workflow()

    # Start the webhook listener
    webhook_handler.start_listener(workflow)

if __name__ == "__main__":
    main()
