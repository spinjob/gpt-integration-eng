import pytest
from functions import get_menu, upsert_menu

def test_get_menu():
    data = get_menu('test')
    assert 'menu' in data

def test_upsert_menu():
    response = upsert_menu('test', {'menu': 'test'})
    assert response.status_code == 200
