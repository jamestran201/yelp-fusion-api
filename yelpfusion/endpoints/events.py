from typing import Any, Dict, Optional

from yelpfusion.endpoint import Endpoint


class Events(Endpoint):
    def get(self, id: str, locale: Optional[str] = None) -> Dict[str, Any]:
        params = {}
        if locale:
            params["locale"] = locale

        return self._get(f"/events/{id}", params=params)
