import pytest
from workflow_manager import WorkflowManager

def test_workflow_manager_init():
    manager = WorkflowManager()
    assert manager is not None

def test_workflow_manager_run_workflow():
    manager = WorkflowManager()
    webhook_data = {"test": "data"}
    assert manager.run_workflow(webhook_data) == True
