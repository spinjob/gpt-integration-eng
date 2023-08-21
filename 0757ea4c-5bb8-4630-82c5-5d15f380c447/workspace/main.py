import json
from flask import Flask, request
from oauth2_client import OAuth2Client
from webhook_handler import WebhookHandler
from workflow_executor import WorkflowExecutor
from error_handler import ErrorHandler

app = Flask(__name__)

marketplace_client = OAuth2Client(client_id='be04e745-844d-4a6c-8fba-f71199dc8f05', client_secret='MD727PM35KZCWP337TKQ')
pos_client = OAuth2Client(client_id='04db98cc-0c84-47e2-b57f-bfd6329c4675', client_secret='NUCGB6VKFLYQBZPMMBLA')

webhook_handler = WebhookHandler()
workflow_executor = WorkflowExecutor(marketplace_client, pos_client)
error_handler = ErrorHandler()

@app.route('/webhook', methods=['POST'])
def handle_webhook():
    try:
        data = webhook_handler.parse_request_body(request.data)
        workflow_executor.execute_workflow(data)
    except Exception as e:
        error_handler.handle_error(e)
    return '', 200

if __name__ == '__main__':
    app.run(port=5000)
