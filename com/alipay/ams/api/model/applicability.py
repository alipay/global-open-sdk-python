import json




class Applicability:
    def __init__(self):
        
        self.__scope = None  # type: str
        self.__price_ids = None  # type: [str]
        

    @property
    def scope(self):
        """
        The applicability scope. Valid values are ALL and SPECIFIC. ALL applies the Credit Grant to all eligible Prices that use the same currency as the Grant and omits priceIds; SPECIFIC applies it only to the Prices specified by priceIds. Maximum length: 8 characters.
        """
        return self.__scope

    @scope.setter
    def scope(self, value):
        self.__scope = value
    @property
    def price_ids(self):
        """
        The Price IDs that the Credit Grant applies to. Required when scope is SPECIFIC and values must be unique; omitted when scope is ALL. Maximum size: 64 elements. Maximum length per item: 64 characters.
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
