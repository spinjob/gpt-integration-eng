import pytest
from apirequester import APIRequester

def test_get_request():
    requester = APIRequester()
    response = requester.get_request("https://partners.cloudkitchens.com/getMenu", {"X-Store-Id": "test-store-id"})
    assert response.status_code == 200

def test_post_request():
    requester = APIRequester()
    response = requester.post_request("https://partners.cloudkitchens.com/upsertMenu", {"categories": {"test-category-id": {"id": "test-category-id", "name": "test-category-name"}}})
    assert response.status_code == 200
