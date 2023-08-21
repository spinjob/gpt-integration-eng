from flask import Flask, request
from workflow import Workflow

app = Flask(__name__)

class WebhookHandler:
    def start_listener(self, workflow: Workflow):
        @app.route('/webhook', methods=['POST'])
        def handle_webhook():
            # Parse the webhook data
            data = request.get_json()

            # Trigger the workflow
            workflow.execute_steps(data)

            return 'OK', 200

        app.run()
