from flask import Flask, request
from .workflow_step import WorkflowStep

app = Flask(__name__)

class WorkflowTrigger:
    def __init__(self, steps):
        self.steps = steps

    @app.route('/webhook', methods=['POST'])
    def handle_webhook():
        data = request.get_json()
        for step in self.steps:
            step.execute(data)
        return '', 200
