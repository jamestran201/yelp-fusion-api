from yelpfusion.endpoints.businesses import Businesses


def test_business_search(requests_mock):
    mock_api = requests_mock.get("https://api.yelp.com/v3/businesses/search", json={})

    Businesses("test-key").search(location="Toronto")

    assert mock_api.called is True


def test_business_search_by_phone_number(requests_mock):
    mock_api = requests_mock.get("https://api.yelp.com/v3/businesses/search/phone", json={})

    Businesses("test-key").search_by_phone_number(phone="11234567890", locale="en_US")

    assert mock_api.called is True


def test_business_details(requests_mock):
    mock_api = requests_mock.get("https://api.yelp.com/v3/businesses/fakebusiness", json={})

    Businesses("test-key").details("fakebusiness", locale="en_US")

    assert mock_api.called is True
