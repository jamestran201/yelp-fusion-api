from yelpfusion.endpoints.autocomplete import Autocomplete


def test_autocomplete_get(requests_mock):
    mock_api = requests_mock.get("https://api.yelp.com/v3/autocomplete", json={})

    Autocomplete("test-key").get(text="sushi")

    assert mock_api.called is True
