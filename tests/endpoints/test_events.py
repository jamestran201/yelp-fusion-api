from yelpfusion.endpoints.events import Events


def test_events_get(requests_mock):
    mock_api = requests_mock.get("https://api.yelp.com/v3/events/abc", json={})

    Events("test-key").get("abc", locale="en_US")

    assert mock_api.called is True
