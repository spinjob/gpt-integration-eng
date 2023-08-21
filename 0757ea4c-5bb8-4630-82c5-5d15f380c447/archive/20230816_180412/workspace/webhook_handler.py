from flask import Flask, request
from workflow import Workflow

app = Flask(__name__)

class WebhookHandler:
    def __init__(self):
        self.workflow = Workflow()

    def start(self):
        app.run(debug=True)

    @app.route('/webhook', methods=['POST'])
    def handle_request(self):
        # Parse the request
        data = request.get_json()
        # Trigger the workflow
        self.workflow.execute(data)
        return '', 200
