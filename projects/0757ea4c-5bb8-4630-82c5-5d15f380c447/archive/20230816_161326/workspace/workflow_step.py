from .api_client import APIClient
from .data_mapper import DataMapper

class WorkflowStep:
    def __init__(self, api_client, data_mapper):
        self.api_client = api_client
        self.data_mapper = data_mapper

    def execute(self, data):
        mapped_data = self.data_mapper.map(data)
        response = self.api_client.post(self.data_mapper.path, mapped_data)
        return response
