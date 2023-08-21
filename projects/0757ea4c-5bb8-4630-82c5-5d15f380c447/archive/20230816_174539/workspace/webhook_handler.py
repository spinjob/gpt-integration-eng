import json

class WebhookHandler:
    def parse_webhook(self, webhook_data):
        # Extract the relevant data from the webhook
        # Assuming the webhook data is a JSON string
        parsed_data = json.loads(webhook_data)
        return parsed_data
