import os
from flask import Flask, request
from webhookhandler import WebhookHandler

app = Flask(__name__)
handler = WebhookHandler()

@app.route('/webhook', methods=['POST'])
def handle_webhook():
    data = request.get_json()
    handler.handle_webhook(data)
    return '', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
