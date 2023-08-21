import requests
from flask import Flask, request

app = Flask(__name__)

class WebhookReceiver:
    def __init__(self):
        pass

    def start(self):
        app.run(host='0.0.0.0', port=5000)

    @app.route('/webhook', methods=['POST'])
    def handle_webhook(self):
        data = request.get_json()
        return 'OK', 200
