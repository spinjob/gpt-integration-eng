from flask import Flask, request

class WebhookTrigger:
    def __init__(self, api_integration):
        self.api_integration = api_integration
        self.app = Flask(__name__)

    def listen(self):
        @self.app.route('/webhook', methods=['POST'])
        def handle_webhook():
            data = request.get_json()
            menu = self.api_integration.get_menu(data['storeId'])
            self.api_integration.upsert_menu(menu)
            return '', 200

        self.app.run(host='0.0.0.0', port=8080)
