import pytest
from workflow import Workflow

def test_execute_step():
    workflow = Workflow(steps=[{'api': 'test', 'method': 'get', 'path': '/test', 'data_mapping': {'test': {'input': {'in': 'body', 'sourcePath': 'test'}, 'output': {'in': 'body', 'outputPath': 'test'}}}}])
    workflow.execute_step(0)
    assert workflow.data == {'test': 'test'}
