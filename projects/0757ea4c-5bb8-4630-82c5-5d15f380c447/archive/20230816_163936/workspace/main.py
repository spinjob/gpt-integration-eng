import json
from flask import Flask, request
from api_client import APIClient
from data_mapper import DataMapper

app = Flask(__name__)
api_client = APIClient()
data_mapper = DataMapper()

@app.route('/webhook', methods=['POST'])
def webhook():
    webhook_data = request.get_json()

    # Step 1: Create Order
    create_order_mapping = json.loads(open('step1_mapping.json').read())
    create_order_data = data_mapper.map_data(webhook_data, create_order_mapping)
    create_order_response = api_client.create_order(create_order_data)

    # Step 2: Update Order Status
    update_order_status_mapping = json.loads(open('step2_mapping.json').read())
    update_order_status_data = data_mapper.map_data(create_order_response, update_order_status_mapping)
    update_order_status_response = api_client.update_order_status(update_order_status_data)

    # Step 3: Get Menu
    get_menu_mapping = json.loads(open('step3_mapping.json').read())
    get_menu_data = data_mapper.map_data(update_order_status_response, get_menu_mapping)
    get_menu_response = api_client.get_menu(get_menu_data)

    # Step 4: Publish Error
    publish_error_mapping = json.loads(open('step4_mapping.json').read())
    publish_error_data = data_mapper.map_data(get_menu_response, publish_error_mapping)
    publish_error_response = api_client.publish_error(publish_error_data)

    return 'Workflow completed', 200

if __name__ == '__main__':
    app.run(port=5000)
