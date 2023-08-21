import os
from webhook_handler import WebhookHandler

def main():
    # Get the webhook URL from environment variables
    webhook_url = os.getenv('WEBHOOK_URL')

    # Create a WebhookHandler instance
    webhook_handler = WebhookHandler(webhook_url)

    # Start the webhook listener
    webhook_handler.start_listener()

if __name__ == '__main__':
    main()
