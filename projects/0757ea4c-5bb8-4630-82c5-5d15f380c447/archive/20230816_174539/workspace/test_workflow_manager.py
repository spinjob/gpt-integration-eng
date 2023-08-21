import pytest
from workflow_manager import WorkflowManager

def test_run_workflow():
    workflow_manager = WorkflowManager()
    webhook_data = {"metadata": {"payload": {"currencyCode": "USD"}}}
    response = workflow_manager.run_workflow(webhook_data)
    assert response == "Workflow completed successfully"
