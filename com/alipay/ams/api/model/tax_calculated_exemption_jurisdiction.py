import json




class TaxCalculatedExemptionJurisdiction:
    def __init__(self):
        
        self.__country = None  # type: str
        self.__region = None  # type: str
        self.__city = None  # type: str
        self.__effective_from = None  # type: str
        

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
    def city(self):
        """
        The city. Maximum length: 64 characters.
        """
        return self.__city

    @city.setter
    def city(self, value):
        self.__city = value
    @property
    def effective_from(self):
        """
        The time when the tax exemption becomes effective. Maximum length: 32 characters.
        """
        return self.__effective_from

    @effective_from.setter
    def effective_from(self, value):
        self.__effective_from = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "country") and self.country is not None:
            params['country'] = self.country
        if hasattr(self, "region") and self.region is not None:
            params['region'] = self.region
        if hasattr(self, "city") and self.city is not None:
            params['city'] = self.city
        if hasattr(self, "effective_from") and self.effective_from is not None:
            params['effectiveFrom'] = self.effective_from
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'country' in response_body:
            self.__country = response_body['country']
        if 'region' in response_body:
            self.__region = response_body['region']
        if 'city' in response_body:
            self.__city = response_body['city']
        if 'effectiveFrom' in response_body:
            self.__effective_from = response_body['effectiveFrom']
