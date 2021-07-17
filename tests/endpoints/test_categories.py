from yelpfusion.endpoints.categories import Categories


def test_categories_all(requests_mock):
    mock_api = requests_mock.get("https://api.yelp.com/v3/categories", json={})

    Categories("test-key").all(locale="fr_CA")

    assert mock_api.called is True


def test_categories_details(requests_mock):
    mock_api = requests_mock.get("https://api.yelp.com/v3/categories/ramen", json={})

    Categories("test-key").details(alias="ramen", locale="fr_CA")

    assert mock_api.called is True
