import pytest
from workflow import Workflow

def test_execute_workflow():
    workflow = Workflow()
    data = {'key': 'value'}
    result = workflow.execute(data)
    assert result == 'Workflow executed'
