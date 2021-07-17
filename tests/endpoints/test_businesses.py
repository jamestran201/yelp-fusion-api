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


def test_business_matches(requests_mock, businesses_endpoint):
    mock_api = requests_mock.get("https://api.yelp.com/v3/businesses/matches", json={})

    businesses_endpoint.matches(
        name="Restaurant", city="Waterloo", state="Ontario", country="Canada", address1="123 Dummy Road"
    )

    assert mock_api.called is True


def test_business_reviews(requests_mock, businesses_endpoint):
    mock_api = requests_mock.get("https://api.yelp.com/v3/businesses/fakebusiness/reviews", json={})

    businesses_endpoint.reviews("fakebusiness", locale="en_US")

    assert mock_api.called is True
