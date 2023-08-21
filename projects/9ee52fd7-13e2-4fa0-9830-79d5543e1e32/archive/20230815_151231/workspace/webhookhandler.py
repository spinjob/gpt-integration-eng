class WebhookHandler:
    def handle_webhook(self, webhook_body):
        # Extract the store ID from the webhook body
        store_id = webhook_body["metadata"]["storeId"]
        return store_id
