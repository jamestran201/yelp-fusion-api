import pytest

from yelpfusion.param_validators.transaction.search_param import SearchParamValidator


@pytest.mark.parametrize(
    "location, latitude, longitude",
    [
        (None, 123.0, 456.0),
        ("Toronto", None, None),
    ],
)
def test_valid_location_latitude_longitude(location, latitude, longitude):
    param = SearchParamValidator(location=location, latitude=latitude, longitude=longitude)

    assert param.location == location
    assert param.latitude == latitude
    assert param.longitude == longitude


def test_missing_location_and_latitude():
    with pytest.raises(ValueError) as e:
        SearchParamValidator(longitude=123.0)

    assert str(e.value) == "location must be provided. Otherwise, both latitude and longitude must be provided."


def test_missing_location_and_longitude():
    with pytest.raises(ValueError) as e:
        SearchParamValidator(latitude=123.0)

    assert str(e.value) == "location must be provided. Otherwise, both latitude and longitude must be provided."
