from typing import Any, Dict

from yelpfusion.endpoint import Endpoint
from yelpfusion.param_validators.autocomplete.param import Param


class Autocomplete(Endpoint):
    def get(self, **params: Any) -> Dict[str, Any]:
        Param(**params)

        return self._get("/autocomplete", params=params)
