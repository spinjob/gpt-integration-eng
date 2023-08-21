from oauth2client import OAuth2Client
from apirequest import APIRequest
from datamapper import DataMapper

class Workflow:
    def __init__(self, steps):
        self.steps = steps
        self.data = {}

    def execute_step(self, index):
        step = self.steps[index]
        client = OAuth2Client(client_id='test', client_secret='test', token_url='https://example.com/token')
        token = client.get_access_token()
        request = APIRequest(url=step['api'], headers={'Authorization': 'Bearer ' + token['access_token']})
        if step['method'] == 'get':
            self.data = request.get(step['path'])
        elif step['method'] == 'post':
            mapper = DataMapper(step['data_mapping'])
            data = mapper.map_data(self.data, 'body')
            self.data = request.post(step['path'], data)
