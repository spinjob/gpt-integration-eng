from api import API
from auth import Auth
from workflow import Workflow
from webhook import Webhook

def main():
    # Initialize the webhook
    webhook = Webhook()

    # Wait for the webhook trigger
    webhook.wait_for_trigger()

    # Initialize the auth objects for both APIs
    auth_pos = Auth(client_id='pos_client_id', client_secret='pos_client_secret', scope='pos_scope')
    auth_marketplace = Auth(client_id='marketplace_client_id', client_secret='marketplace_client_secret', scope='marketplace_scope')

    # Initialize the API objects for both APIs
    api_pos = API(base_url='https://partners.cloudkitchens.com', auth=auth_pos)
    api_marketplace = API(base_url='https://partners.cloudkitchens.com', auth=auth_marketplace)

    # Initialize the workflow
    workflow = Workflow(api_pos=api_pos, api_marketplace=api_marketplace)

    # Execute the workflow
    workflow.execute()

if __name__ == '__main__':
    main()
