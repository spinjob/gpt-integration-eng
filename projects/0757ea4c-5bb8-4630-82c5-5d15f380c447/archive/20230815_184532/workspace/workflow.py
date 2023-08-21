from api import API
from data_mapping import DataMapping

class Workflow:
    def __init__(self, trigger_data):
        self.trigger_data = trigger_data

    def execute_step(self, api_id, method, path, data_mapping_json, previous_step_data=None):
        api = API(api_id)
        data_mapping = DataMapping(data_mapping_json)
        source_data = previous_step_data or self.trigger_data
        data = data_mapping.map_data(source_data)
        return api.make_request(method, path, data=data)
