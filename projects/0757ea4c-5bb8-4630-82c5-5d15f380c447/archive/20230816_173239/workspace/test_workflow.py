import pytest
from workflow import Workflow

def test_workflow_steps():
    workflow = Workflow()
    response = workflow.execute_steps()
    assert response is True
