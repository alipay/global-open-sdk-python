import json




class CustomerTaxId:
    def __init__(self):
        
        self.__value = None  # type: str
        self.__country = None  # type: str
        self.__region = None  # type: str
        self.__type = None  # type: str
        

    @property
    def value(self):
        """
        Tax registration number. Supply a nonblank value.
        """
        return self.__value

    @value.setter
    def value(self, value):
        self.__value = value
    @property
    def country(self):
        """
        Two-letter ISO 3166-1 code for the issuing country. Supply a nonblank value such as US.
        """
        return self.__country

    @country.setter
    def country(self, value):
        self.__country = value
    @property
    def region(self):
        """
        ISO 3166-2 subdivision code, such as US-CA. The prefix must match country. Omitted or null means no subdivision.
        """
        return self.__region

    @region.setter
    def region(self, value):
        self.__region = value
    @property
    def type(self):
        """
        Display label such as VAT or TIN. Omitted or null means no label.
        """
        return self.__type

    @type.setter
    def type(self, value):
        self.__type = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "value") and self.value is not None:
            params['value'] = self.value
        if hasattr(self, "country") and self.country is not None:
            params['country'] = self.country
        if hasattr(self, "region") and self.region is not None:
            params['region'] = self.region
        if hasattr(self, "type") and self.type is not None:
            params['type'] = self.type
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'value' in response_body:
            self.__value = response_body['value']
        if 'country' in response_body:
            self.__country = response_body['country']
        if 'region' in response_body:
            self.__region = response_body['region']
        if 'type' in response_body:
            self.__type = response_body['type']
