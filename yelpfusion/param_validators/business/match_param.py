from dataclasses import dataclass
from typing import Optional


@dataclass
class MatchParamValidator:
    name: str
    city: str
    state: str
    country: str
    address: str
    address2: Optional[str] = None
    address3: Optional[str] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    phone: Optional[str] = None
    zip_code: Optional[str] = None
    yelp_business_id: Optional[str] = None
    limit: Optional[int] = None
    match_threshold: Optional[str] = None
