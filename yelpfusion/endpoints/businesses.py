from typing import Any, Dict, Optional

from yelpfusion.endpoint import Endpoint
from yelpfusion.param_validators.business.match_param import MatchParamValidator
from yelpfusion.param_validators.business.search_param import SearchParamValidator


class Businesses(Endpoint):
    def search(self, **params: Any) -> Dict[str, Any]:
        SearchParamValidator(**params)

        return self._get_request("/businesses/search", params)

    def search_by_phone_number(self, phone: str, locale: Optional[str] = None) -> Dict[str, Any]:
        params = {"phone": phone}
        if locale:
            params["locale"] = locale

        return self._get_request("/businesses/search/phone", params=params)

    def details(self, business_id: str, locale: Optional[str] = None) -> Dict[str, Any]:
        params = {}
        if locale:
            params["locale"] = locale

        return self._get_request(f"/businesses/{business_id}", params=params)

    def matches(self, **params: Any) -> Dict[str, Any]:
        MatchParamValidator(**params)

        return self._get_request("/businesses/matches", params=params)
