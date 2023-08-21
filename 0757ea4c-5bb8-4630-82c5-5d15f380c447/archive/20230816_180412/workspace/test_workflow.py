import pytest
from workflow import Workflow

def test_execute():
    workflow = Workflow()
    workflow.execute()
    assert workflow.steps_executed == True
