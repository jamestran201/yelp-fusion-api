from typing import Any, Dict

from yelpfusion.endpoint import Endpoint
from yelpfusion.param_validators.transaction.search_param import SearchParamValidator


class Transactions(Endpoint):
    def search(self, transaction_type: str, **params: Any) -> Dict[str, Any]:
        SearchParamValidator(**params)

        return self._get(f"/transactions/{transaction_type}/search", params=params)
