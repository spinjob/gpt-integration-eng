from flask import Flask, request
from workflow import Workflow

app = Flask(__name__)
workflow = Workflow()

@app.route('/webhook', methods=['POST'])
def handle_webhook():
    data = request.get_json()
    workflow.execute(data)
    return '', 200

if __name__ == '__main__':
    app.run(port=5000)
