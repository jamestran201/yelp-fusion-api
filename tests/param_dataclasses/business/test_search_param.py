import pytest

from yelpfusion.param_dataclasses.business.search_param import SearchParam


@pytest.mark.parametrize(
    "location, latitude, longitude",
    [
        (None, 123.0, 456.0),
        ("Toronto", None, None),
    ],
)
def test_valid_location_latitude_longitude(location, latitude, longitude):
    param = SearchParam(location=location, latitude=latitude, longitude=longitude)

    assert param.location == location
    assert param.latitude == latitude
    assert param.longitude == longitude


def test_missing_location_and_latitude():
    with pytest.raises(ValueError):
        SearchParam(longitude=123.0)


def test_missing_location_and_longitude():
    with pytest.raises(ValueError):
        SearchParam(latitude=123.0)
