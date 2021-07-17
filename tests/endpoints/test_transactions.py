from yelpfusion.endpoints.transactions import Transactions


def test_transaction_search(requests_mock):
    mock_api = requests_mock.get("https://api.yelp.com/v3/transactions/pickup/search", json={})

    Transactions("test-key").search("pickup", location="Markham")

    assert mock_api.called is True
