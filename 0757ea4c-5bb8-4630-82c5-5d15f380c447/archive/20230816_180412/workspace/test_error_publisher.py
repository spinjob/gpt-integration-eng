import pytest
from error_publisher import ErrorPublisher

def test_publish():
    publisher = ErrorPublisher()
    publisher.publish(Exception("Test error"))
    assert publisher.error_published == True
