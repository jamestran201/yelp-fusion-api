import pytest

from yelpfusion.endpoints.businesses import Businesses


@pytest.fixture
def businesses_endpoint():
    return Businesses("test-key")


def test_business_search(requests_mock, businesses_endpoint):
    mock_api = requests_mock.get("https://api.yelp.com/v3/businesses/search", json={})

    businesses_endpoint.search(location="Toronto")

    assert mock_api.called is True


def test_business_search_by_phone_number(requests_mock, businesses_endpoint):
    mock_api = requests_mock.get("https://api.yelp.com/v3/businesses/search/phone", json={})

    businesses_endpoint.search_by_phone_number(phone="11234567890", locale="en_US")

    assert mock_api.called is True


def test_business_details(requests_mock, businesses_endpoint):
    mock_api = requests_mock.get("https://api.yelp.com/v3/businesses/fakebusiness", json={})

    businesses_endpoint.details("fakebusiness", locale="en_US")

    assert mock_api.called is True
