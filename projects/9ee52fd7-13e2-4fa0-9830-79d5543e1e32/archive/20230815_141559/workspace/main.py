import json
from webhook_handler import WebhookHandler
from oauth2_authenticator import OAuth2Authenticator
from api_requester import APIRequester
from data_mapper import DataMapper
from workflow_executor import WorkflowExecutor
from error_handler import ErrorHandler

def main(request, credentials, steps):
    try:
        # Initialize classes
        handler = WebhookHandler()
        authenticator = OAuth2Authenticator()
        requester = APIRequester()
        mapper = DataMapper()
        executor = WorkflowExecutor()
        error_handler = ErrorHandler()

        # Handle webhook trigger
        data = handler.handle_trigger(request)

        # Perform OAuth2 authentication
        token = authenticator.authenticate(credentials)

        # Execute workflow steps
        for step in steps:
            # Map data
            output = mapper.map_data(data, step['mapping'])

            # Add token to headers
            step['headers']['Authorization'] = f'Bearer {token}'

            # Perform API request
            response = requester.request(step['method'], step['url'], step['headers'], output)

            # Update data with response
            data.update(response)

        return data

    except Exception as e:
        # Handle error
        message = error_handler.handle_error(e)
        return {'error': message}

if __name__ == "__main__":
    request = json.loads(input())
    credentials = {'client_id': 'your_client_id', 'client_secret': 'your_client_secret', 'grant_type': 'client_credentials'}
    steps = [{'method': 'GET', 'url': 'https://api.example.com/data', 'headers': {}, 'mapping': {'key': 'value'}}]
    print(main(request, credentials, steps))
