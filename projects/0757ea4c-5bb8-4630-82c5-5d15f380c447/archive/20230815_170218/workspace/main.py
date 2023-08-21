from apiclient import APIClient
from oauth2clientcredentials import OAuth2ClientCredentials
from workflowtrigger import WorkflowTrigger
from workflowstep import WorkflowStep

def main():
    marketplace_api_client = APIClient('https://partners.cloudkitchens.com')
    pos_api_client = APIClient('https://partners.cloudkitchens.com')

    marketplace_auth = OAuth2ClientCredentials('client_id', 'client_secret', '/v1/auth/token')
    pos_auth = OAuth2ClientCredentials('client_id', 'client_secret', '/v1/auth/token')

    marketplace_api_client.headers = {'Authorization': 'Bearer ' + marketplace_auth.generate_token()}
    pos_api_client.headers = {'Authorization': 'Bearer ' + pos_auth.generate_token()}

    workflow_steps = [
        WorkflowStep(pos_api_client, 'createOrder', '/v1/orders', data_mapping_1),
        WorkflowStep(marketplace_api_client, 'updateOrderStatus', '/v1/orders/{orderId}', data_mapping_2),
        WorkflowStep(pos_api_client, 'getMenu', '/v1/menus', data_mapping_3),
        WorkflowStep(marketplace_api_client, 'publishError', '/v1/errors', data_mapping_4)
    ]

    workflow_trigger = WorkflowTrigger(workflow_steps)
    workflow_trigger.start()

if __name__ == '__main__':
    main()
