import json




class TaxId:
    def __init__(self):
        
        self.__value = None  # type: str
        self.__country = None  # type: str
        self.__region = None  # type: str
        

    @property
    def value(self):
        """
        The value of the amount as a positive integer in the smallest currency unit. Maximum length: 64 characters.
        """
        return self.__value

    @value.setter
    def value(self, value):
        self.__value = value
    @property
    def country(self):
        """
        The country or region code. Maximum length: 2 characters.
        """
        return self.__country

    @country.setter
    def country(self, value):
        self.__country = value
    @property
    def region(self):
        """
        The region. Maximum length: 10 characters. Note: See documentation for details.
        """
        return self.__region

    @region.setter
    def region(self, value):
        self.__region = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "value") and self.value is not None:
            params['value'] = self.value
        if hasattr(self, "country") and self.country is not None:
            params['country'] = self.country
        if hasattr(self, "region") and self.region is not None:
            params['region'] = self.region
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
