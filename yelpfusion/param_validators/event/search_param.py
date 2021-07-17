from dataclasses import dataclass
from typing import List, Optional, Tuple, Union

StringListLike = Union[List[str], Tuple[str, ...]]


@dataclass
class SearchParamValidator:
    locale: Optional[str] = None
    offset: Optional[int] = None
    limit: Optional[int] = None
    sort_by: Optional[str] = None
    sort_on: Optional[str] = None
    start_date: Optional[int] = None
    end_date: Optional[int] = None
    categories: Optional[int] = None
    is_free: Optional[bool] = None
    location: Optional[str] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    radius: Optional[int] = None
    excluded_events: Optional[StringListLike] = None
