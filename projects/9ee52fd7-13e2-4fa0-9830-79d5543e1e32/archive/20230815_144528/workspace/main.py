import requests
import json
from flask import Flask, request
from oauth2_authenticator import OAuth2Authenticator
from http_requester import HttpRequester
from data_mapper import DataMapper

app = Flask(__name__)

authenticator = OAuth2Authenticator()
requester = HttpRequester()
mapper = DataMapper()

@app.route('/webhook', methods=['POST'])
def webhook():
    # Handle webhook trigger
    webhook_data = request.json

    # Step 1: getMenu
    store_id = webhook_data['metadata']['storeId']
    headers = {'X-Store-Id': store_id}
    menu = requester.send_request('2389bc50-2646-4e94-bb34-86c9ea23cd7e', 'GET', '/menu', headers, None)

    # Step 2: upsertMenu
    headers = {'Content-Type': 'application/json'}
    body = mapper.map_data(menu, webhook_data)
    requester.send_request('98ef9a91-f0ca-4e0a-acd3-4618904fd6b4', 'POST', '/menu', headers, body)

    return 'OK', 200

if __name__ == '__main__':
    app.run(port=5000)
