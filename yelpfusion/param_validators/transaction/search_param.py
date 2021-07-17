from dataclasses import dataclass
from typing import Optional


@dataclass
class SearchParamValidator:
    location: Optional[str] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None

    def __post_init__(self):
        self._validate_location_lat_long_presence()

    def _validate_location_lat_long_presence(self) -> None:
        if not self.location and (not self.latitude or not self.longitude):
            raise ValueError("location must be provided. Otherwise, both latitude and longitude must be provided.")
