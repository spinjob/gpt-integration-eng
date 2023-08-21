pip install --user virtualenv
python3 -m venv env
source env/bin/activate
pip install flask requests python-dotenv

export FLASK_APP=main.py
export POS_API_CLIENT_ID='your_pos_api_client_id'
export POS_API_CLIENT_SECRET='your_pos_api_client_secret'
export POS_API_TOKEN_URL='your_pos_api_token_url'
export MARKETPLACE_API_CLIENT_ID='your_marketplace_api_client_id'
export MARKETPLACE_API_CLIENT_SECRET='your_marketplace_api_client_secret'
export MARKETPLACE_API_TOKEN_URL='your_marketplace_api_token_url'
flask run
