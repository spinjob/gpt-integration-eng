import json

class WebhookHandler:
    def parse_request_body(self, body):
        return json.loads(body)
