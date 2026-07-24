import json




class Applicability:
    def __init__(self):
        
        self.__scope = None  # type: str
        self.__price_ids = None  # type: str
        

    @property
    def scope(self):
        """
        The scope. Maximum length: 8 characters.
        """
        return self.__scope

    @scope.setter
    def scope(self, value):
        self.__scope = value
    @property
    def price_ids(self):
        """
        The price ids. Note: See documentation for details.
        """
        return self.__price_ids

    @price_ids.setter
    def price_ids(self, value):
        self.__price_ids = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "scope") and self.scope is not None:
            params['scope'] = self.scope
        if hasattr(self, "price_ids") and self.price_ids is not None:
            params['priceIds'] = self.price_ids
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'scope' in response_body:
            self.__scope = response_body['scope']
        if 'priceIds' in response_body:
            self.__price_ids = response_body['priceIds']
