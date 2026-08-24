import json




class TaxCalculatedTaxId:
    def __init__(self):
        
        self.__value = None  # type: str
        self.__country = None  # type: str
        self.__region = None  # type: str
        self.__name = None  # type: str
        

    @property
    def value(self):
        """
        The customer tax ID value. Maximum length: 64 characters.
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
        The region. Maximum length: 10 characters.
        """
        return self.__region

    @region.setter
    def region(self, value):
        self.__region = value
    @property
    def name(self):
        """
        The customer name recorded for tax purposes. Maximum length: 256 characters.
        """
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "value") and self.value is not None:
            params['value'] = self.value
        if hasattr(self, "country") and self.country is not None:
            params['country'] = self.country
        if hasattr(self, "region") and self.region is not None:
            params['region'] = self.region
        if hasattr(self, "name") and self.name is not None:
            params['name'] = self.name
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
        if 'name' in response_body:
            self.__name = response_body['name']
