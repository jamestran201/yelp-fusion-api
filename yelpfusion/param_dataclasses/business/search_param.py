from dataclasses import dataclass
from typing import Optional


@dataclass
class SearchParam:
    term: Optional[str] = None
    location: Optional[str] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    radius: Optional[int] = None
    categories: Optional[str] = None
    locale: Optional[str] = None
    limit: Optional[int] = None
    offset: Optional[int] = None
    sort_by: Optional[str] = None
    price: Optional[str] = None
    open_now: Optional[bool] = False
    open_at: Optional[int] = None
    attributes: Optional[str] = None

    def __post_init__(self):
        self._validate_location_lat_long_presence()
        self._validate_open_now_and_open_at()

    def _validate_location_lat_long_presence(self) -> None:
        if not self.location and (not self.latitude or not self.longitude):
            raise ValueError(
                "location must be provided. Otherwise, both latitude and longitude must be provided."
            )

    def _validate_open_now_and_open_at(self) -> None:
        if self.open_now and self.open_at is not None:
            raise ValueError("open_at and open_now cannot be used together.")
