class WebhookHandler:
    def handle_trigger(self, request):
        # Extract necessary data from webhook request body
        data = request['body']['metadata']
        return data
