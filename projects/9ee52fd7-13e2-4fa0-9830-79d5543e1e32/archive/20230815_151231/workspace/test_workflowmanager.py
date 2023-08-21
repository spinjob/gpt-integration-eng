import pytest
from workflowmanager import WorkflowManager

def test_start_workflow():
    manager = WorkflowManager()
    webhook_body = {"metadata": {"storeId": "test-store-id"}}
    result = manager.start_workflow(webhook_body)
    assert result == True
