from yelpfusion.endpoints.businesses import Businesses


def test_business_search(request_mock):
    mock_search = request_mock.get("https://api.yelp.com/v3/businesses/search", json={})

    Businesses("test-key").search(location="Toronto")

    assert mock_search.called is True
