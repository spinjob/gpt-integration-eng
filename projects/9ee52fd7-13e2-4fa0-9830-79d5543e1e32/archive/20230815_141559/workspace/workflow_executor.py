class WorkflowExecutor:
    def execute_step(self, step):
        # Execute workflow step and return response
        response = self.requester.request(step['method'], step['url'], step['headers'], step['body'])
        return response
