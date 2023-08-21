import pytest
from step import Step

def test_execute():
    step = Step()
    step.execute()
    assert step.request_made == True
