class ErrorHandler:
    def __init__(self, api_client):
        self.api_client = api_client

    def handle_error(self, error):
        self.api_client.request('/error', {'error': str(error)})
