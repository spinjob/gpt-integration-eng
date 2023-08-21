from datamapper import DataMapper

class WorkflowStep:
    def __init__(self, api_client, method, path, data_mapping):
        self.api_client = api_client
        self.method = method
        self.path = path
        self.data_mapper = DataMapper(data_mapping)

    def execute(self, input_data):
        mapped_data = self.data_mapper.map(input_data)
        response = getattr(self.api_client, self.method)(self.path, data=mapped_data)
        return response.json()
