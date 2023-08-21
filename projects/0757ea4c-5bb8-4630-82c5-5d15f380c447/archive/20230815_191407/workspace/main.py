from flask import Flask, request
from api_client import APIClient
from data_mapper import DataMapper

app = Flask(__name__)
api_client = APIClient()
data_mapper = DataMapper()

@app.route('/webhook', methods=['POST'])
def webhook():
    webhook_data = request.json
    step1_data = data_mapper.map(webhook_data, 'step1.json')
    step1_response = api_client.create_order(step1_data)
    step2_data = data_mapper.map(step1_response, 'step2.json')
    step2_response = api_client.update_order_status(step2_data)
    step3_data = data_mapper.map(step2_response, 'step3.json')
    step3_response = api_client.get_menu(step3_data)
    step4_data = data_mapper.map(step3_response, 'step4.json')
    api_client.publish_error(step4_data)
    return '', 200

if __name__ == '__main__':
    app.run(port=5000)
