from flask import Flask, request
from workflow import Workflow

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    trigger_data = request.json
    workflow = Workflow(trigger_data)
    step_1_data = workflow.execute_step('98ef9a91-f0ca-4e0a-acd3-4618904fd6b4', 'POST', '/createOrder', step_1_data_mapping_json)
    step_2_data = workflow.execute_step('2389bc50-2646-4e94-bb34-86c9ea23cd7e', 'POST', '/updateOrderStatus/{orderId}', step_2_data_mapping_json, step_1_data)
    step_3_data = workflow.execute_step('98ef9a91-f0ca-4e0a-acd3-4618904fd6b4', 'GET', '/getMenu', step_3_data_mapping_json, step_2_data)
    step_4_data = workflow.execute_step('2389bc50-2646-4e94-bb34-86c9ea23cd7e', 'POST', '/publishError', step_4_data_mapping_json, step_3_data)
    return 'OK', 200

if __name__ == '__main__':
    app.run(port=5000)
