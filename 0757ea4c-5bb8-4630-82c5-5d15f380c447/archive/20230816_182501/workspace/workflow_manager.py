class WorkflowManager:
    def __init__(self, webhook_receiver, api_client, data_mapper):
        self.webhook_receiver = webhook_receiver
        self.api_client = api_client
        self.data_mapper = data_mapper

    def run_workflow(self):
        webhook_data = self.webhook_receiver.handle_webhook()
        mapped_data = self.data_mapper.map_data(webhook_data)
        response = self.api_client.request('/endpoint', mapped_data)
        return response
