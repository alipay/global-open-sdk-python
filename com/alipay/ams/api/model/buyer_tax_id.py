import json




class BuyerTaxId:
    def __init__(self):
        
        self.__country = None  # type: str
        self.__region = None  # type: str
        self.__value = None  # type: str
        

    @property
    def country(self):
        """
        The two-letter ISO 3166-1 alpha-2 country or region code used to validate the tax ID. Maximum length: 2 characters.
        """
        return self.__country

    @country.setter
    def country(self, value):
        self.__country = value
    @property
    def region(self):
        """
        The two-character country-specific subdivision code. Required only when the applicable tax authority or country or region rule requires subdivision-level identification. Maximum length: 2 characters.
        """
        return self.__region

    @region.setter
    def region(self, value):
        self.__region = value
    @property
    def value(self):
        """
        The buyer tax ID value. The accepted format is country-specific. Maximum length: 64 characters.
        """
        return self.__value

    @value.setter
    def value(self, value):
        self.__value = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "country") and self.country is not None:
            params['country'] = self.country
        if hasattr(self, "region") and self.region is not None:
            params['region'] = self.region
        if hasattr(self, "value") and self.value is not None:
            params['value'] = self.value
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'country' in response_body:
            self.__country = response_body['country']
        if 'region' in response_body:
            self.__region = response_body['region']
        if 'value' in response_body:
            self.__value = response_body['value']
