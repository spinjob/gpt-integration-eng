The code provided above seems to be correct and well-structured. However, there are a few points that need to be addressed:

1. The `client_id`, `client_secret`, and `token_url` are hardcoded in the `main.py` file. It's better to use environment variables or a configuration file to store these sensitive data.

2. The `get_menu` and `upsert_menu` methods in the `APIIntegration` class do not handle the case when the token is not yet generated. We need to ensure that the token is generated before making the API request.

3. The `listen` method in the `WebhookTrigger` class is not implemented. We need to implement this method to start listening for the webhook.

4. The `map_data` method in the `DataMapping` class is not implemented. We need to implement this method to map the data from the `get_menu` response to the `upsert_menu` request.

Here is the updated code:

`main.py`
