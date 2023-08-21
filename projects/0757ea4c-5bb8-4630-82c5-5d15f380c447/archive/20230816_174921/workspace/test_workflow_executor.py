import pytest
from workflow_executor import WorkflowExecutor

def test_execute_step():
    executor = WorkflowExecutor()
    response = executor.execute_step('step1', {'test': 'data'})
    assert response.status_code == 200

def test_execute_workflow():
    executor = WorkflowExecutor()
    response = executor.execute_workflow(['step1', 'step2'], {'test': 'data'})
    assert response.status_code == 200
