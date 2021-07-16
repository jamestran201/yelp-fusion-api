from yelpfusion.endpoints.businesses import Businesses


class Api:
    def __init__(self, api_key: str):
        self.businesses = Businesses(api_key)
