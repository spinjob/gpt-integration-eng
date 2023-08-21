import pytest
from workflow_executor import WorkflowExecutor

def test_execute_step():
    executor = WorkflowExecutor()
    step = {"api": "Point-of-Sale API", "method": "GET", "url": "/menu", "headers": {"X-Store-Id": "123"}}
    response = executor.execute_step(step)
    assert isinstance(response, dict)
