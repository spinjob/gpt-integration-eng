import json
from flask import Flask, request
from api_client import APIClient
from data_mapper import DataMapper

app = Flask(__name__)
api_client = APIClient()
data_mapper = DataMapper()

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()
    trigger_data = data_mapper.map_trigger_data(data)
    step1_data = api_client.create_order(trigger_data)
    step2_data = api_client.update_order_status(step1_data)
    step3_data = api_client.get_menu(step2_data)
    step4_data = api_client.publish_error(step3_data)
    return json.dumps(step4_data), 200

if __name__ == '__main__':
    app.run(port=5000)
