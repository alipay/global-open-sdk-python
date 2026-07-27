import json



from com.alipay.ams.api.request.alipay_request import AlipayRequest

class AlipayPriceUpdateRequest(AlipayRequest):
    def __init__(self):
        super(AlipayPriceUpdateRequest, self).__init__("/ams/api/v1/billing/price/update") 

        self.__price_id = None  # type: str
        self.__name = None  # type: str
        self.__metadata = None  # type: {str: (str,)}
        self.__metadata_keys_to_remove = None  # type: str
        self.__active = None  # type: bool
        

    @property
    def price_id(self):
        """
        The price ID. Maximum length: 32 characters.
        """
        return self.__price_id

    @price_id.setter
    def price_id(self, value):
        self.__price_id = value
    @property
    def name(self):
        """
        The name. Maximum length: 128 characters.
        """
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value
    @property
    def metadata(self):
        """
        Custom metadata for special use cases. Maximum length: 20 characters. Note: See documentation for details.
        """
        return self.__metadata

    @metadata.setter
    def metadata(self, value):
        self.__metadata = value
    @property
    def metadata_keys_to_remove(self):
        """
        The metadata keys to remove. Maximum length: 20 characters.
        """
        return self.__metadata_keys_to_remove

    @metadata_keys_to_remove.setter
    def metadata_keys_to_remove(self, value):
        self.__metadata_keys_to_remove = value
    @property
    def active(self):
        """
        The active.
        """
        return self.__active

    @active.setter
    def active(self, value):
        self.__active = value


    def to_ams_json(self): 
        json_str = json.dumps(obj=self.to_ams_dict(), default=lambda o: o.to_ams_dict(), indent=3) 
        return json_str


    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "price_id") and self.price_id is not None:
            params['priceId'] = self.price_id
        if hasattr(self, "name") and self.name is not None:
            params['name'] = self.name
        if hasattr(self, "metadata") and self.metadata is not None:
            params['metadata'] = self.metadata
        if hasattr(self, "metadata_keys_to_remove") and self.metadata_keys_to_remove is not None:
            params['metadataKeysToRemove'] = self.metadata_keys_to_remove
        if hasattr(self, "active") and self.active is not None:
            params['active'] = self.active
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'priceId' in response_body:
            self.__price_id = response_body['priceId']
        if 'name' in response_body:
            self.__name = response_body['name']
        if 'metadata' in response_body:
            self.__metadata = response_body['metadata']
        if 'metadataKeysToRemove' in response_body:
            self.__metadata_keys_to_remove = response_body['metadataKeysToRemove']
        if 'active' in response_body:
            self.__active = response_body['active']
