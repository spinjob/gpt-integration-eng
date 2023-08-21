import pytest
from main import main

def test_main():
    webhook_data = {"metadata": {"payload": {"currencyCode": "USD"}}}
    response = main(webhook_data)
    assert response == "Workflow completed successfully"
