import pytest
from workflowmanager import WorkflowManager

def test_create_order():
    manager = WorkflowManager()
    response = manager.create_order('order_data')
    assert response.status_code == 200

def test_update_order_status():
    manager = WorkflowManager()
    response = manager.update_order_status('order_id', 'status')
    assert response.status_code == 200

def test_get_menu():
    manager = WorkflowManager()
    response = manager.get_menu('store_id')
    assert response.status_code == 200

def test_publish_error():
    manager = WorkflowManager()
    response = manager.publish_error('error_code')
    assert response.status_code == 200
