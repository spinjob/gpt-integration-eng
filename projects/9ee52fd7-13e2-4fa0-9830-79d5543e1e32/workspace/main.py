import os
from oauth2_client import OAuth2Client
from api_integration import APIIntegration
from webhook_trigger import WebhookTrigger

def main():
    # Initialize OAuth2 clients for both APIs
    pos_api_client = OAuth2Client(client_id=os.getenv('POS_API_CLIENT_ID'), client_secret=os.getenv('POS_API_CLIENT_SECRET'), token_url=os.getenv('POS_API_TOKEN_URL'))
    marketplace_api_client = OAuth2Client(client_id=os.getenv('MARKETPLACE_API_CLIENT_ID'), client_secret=os.getenv('MARKETPLACE_API_CLIENT_SECRET'), token_url=os.getenv('MARKETPLACE_API_TOKEN_URL'))

    # Generate tokens
    pos_api_client.generate_token()
    marketplace_api_client.generate_token()

    # Initialize API integration
    api_integration = APIIntegration(pos_api_client, marketplace_api_client)

    # Initialize webhook trigger
    webhook_trigger = WebhookTrigger(api_integration)

    # Start listening for webhook
    webhook_trigger.listen()

if __name__ == "__main__":
    main()
