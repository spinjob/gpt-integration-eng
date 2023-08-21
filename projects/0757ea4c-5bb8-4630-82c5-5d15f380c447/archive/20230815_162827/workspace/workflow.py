class Workflow:
    def __init__(self, api):
        self.api = api

    def execute(self, workflow_trigger, workflow_steps, data_mapping):
        # Execute each step in the workflow
        for step in workflow_steps:
            # Map the data for the step
            data = data_mapping.map_data(step['data_mapping'])

            # Send the API request for the step
            self.api.request(step['method'], step['url'], headers=step['headers'], data=data)
