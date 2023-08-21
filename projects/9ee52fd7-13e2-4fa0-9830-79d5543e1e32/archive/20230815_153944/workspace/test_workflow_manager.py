import pytest
from workflow_manager import WorkflowManager

def test_execute_workflow():
    manager = WorkflowManager()
    assert manager.execute_workflow({}) == True, "Workflow execution should be successful"
