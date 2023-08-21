import pytest
from workflow_executor import WorkflowExecutor

def test_execute_step():
    executor = WorkflowExecutor()
    step = {
        "api_id": "2389bc50-2646-4e94-bb34-86c9ea23cd7e",
        "method": "GET",
        "path": "/menu",
        "headers": {"X-Store-Id": "test-store-id"},
        "body": None
    }
    response = executor.execute_step(step)
    assert isinstance(response, dict)
