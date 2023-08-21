from workflow import Workflow

class WebhookHandler:
    def __init__(self):
        self.workflow = Workflow()

    def handle_webhook(self, data):
        self.workflow.execute(data)
