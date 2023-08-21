from flask import Flask, request
from threading import Thread

class WorkflowTrigger:
    def __init__(self, workflow):
        self.workflow = workflow
        self.app = Flask(__name__)

    def start(self):
        @self.app.route('/webhook', methods=['POST'])
        def handle_webhook():
            self.workflow.execute(request.json)
            return '', 200

        Thread(target=self.app.run).start()
