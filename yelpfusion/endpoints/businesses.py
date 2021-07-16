from typing import Any, Dict

import requests

from yelpfusion.param_validators.business.search_param import SearchParamValidator

BASE_URL = "https://api.yelp.com/v3"


class Businesses:
    def __init__(self, api_key: str):
        self.api_key = api_key

    def search(self, **params: Any) -> Dict[str, Any]:
        SearchParamValidator(**params)

        response = requests.get(f"{BASE_URL}/businesses/search", params=params, headers=self._request_header())
        response.raise_for_status()

        return response.json()

    def _request_header(self) -> Dict[str, str]:
        return {"Authorization": f"Bearer {self.api_key}"}
