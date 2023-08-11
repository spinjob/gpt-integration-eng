import pytest
from string_processor import reverse_string

class TestStringProcessor:
    def test_reverse_string(self):
        assert reverse_string('hello') == 'olleh'
