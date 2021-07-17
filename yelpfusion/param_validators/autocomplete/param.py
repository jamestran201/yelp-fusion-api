from dataclasses import dataclass
from typing import Optional


@dataclass
class Param:
    text: str
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    locale: Optional[str] = None
