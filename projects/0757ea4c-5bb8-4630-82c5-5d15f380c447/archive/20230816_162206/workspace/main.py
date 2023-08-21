from flask import Flask, request
from api import PointOfSaleAPI, MarketplaceAPI
from data_mapping import DataMapper

app = Flask(__name__)

pos_api = PointOfSaleAPI()
marketplace_api = MarketplaceAPI()
data_mapper = DataMapper()

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json

    # Step 1: Create order in Point-of-Sale API
    mapped_data = data_mapper.map(data, 'createOrder')
    pos_api.create_order(mapped_data)

    # Step 2: Update order status in Marketplace API
    mapped_data = data_mapper.map(data, 'updateOrderStatus')
    marketplace_api.update_order_status(mapped_data)

    # Step 3: Get menu from Point-of-Sale API
    mapped_data = data_mapper.map(data, 'getMenu')
    pos_api.get_menu(mapped_data)

    # Step 4: Publish error in Marketplace API
    mapped_data = data_mapper.map(data, 'publishError')
    marketplace_api.publish_error(mapped_data)

    return '', 200

if __name__ == '__main__':
    app.run(port=5000)
