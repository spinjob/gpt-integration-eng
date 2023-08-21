import pytest
from workflow import Workflow

def test_workflow():
    workflow = Workflow()
    assert workflow.perform_step() is None
