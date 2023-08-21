import pytest
from api_integration import APIIntegration

def test_get_menu():
    integration = APIIntegration()
    menu = integration.get_menu(store_id='test_store_id')
    assert isinstance(menu, dict)

def test_upsert_menu():
    integration = APIIntegration()
    menu = {'test': 'menu'}
    response = integration.upsert_menu(menu=menu)
    assert response.status_code == 200
