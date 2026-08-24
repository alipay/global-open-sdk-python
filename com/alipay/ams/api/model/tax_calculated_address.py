import json




class TaxCalculatedAddress:
    def __init__(self):
        
        self.__country = None  # type: str
        self.__region = None  # type: str
        self.__county = None  # type: str
        self.__city = None  # type: str
        self.__district = None  # type: str
        self.__line1 = None  # type: str
        self.__line2 = None  # type: str
        self.__postal_code = None  # type: str
        

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
    def county(self):
        """
        The county. Maximum length: 64 characters.
        """
        return self.__county

    @county.setter
    def county(self, value):
        self.__county = value
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
    def district(self):
        """
        The district. Maximum length: 64 characters.
        """
        return self.__district

    @district.setter
    def district(self, value):
        self.__district = value
    @property
    def line1(self):
        """
        The first address line. Maximum length: 256 characters.
        """
        return self.__line1

    @line1.setter
    def line1(self, value):
        self.__line1 = value
    @property
    def line2(self):
        """
        The second address line. Maximum length: 256 characters.
        """
        return self.__line2

    @line2.setter
    def line2(self, value):
        self.__line2 = value
    @property
    def postal_code(self):
        """
        The postal code. Maximum length: 16 characters.
        """
        return self.__postal_code

    @postal_code.setter
    def postal_code(self, value):
        self.__postal_code = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "country") and self.country is not None:
            params['country'] = self.country
        if hasattr(self, "region") and self.region is not None:
            params['region'] = self.region
        if hasattr(self, "county") and self.county is not None:
            params['county'] = self.county
        if hasattr(self, "city") and self.city is not None:
            params['city'] = self.city
        if hasattr(self, "district") and self.district is not None:
            params['district'] = self.district
        if hasattr(self, "line1") and self.line1 is not None:
            params['line1'] = self.line1
        if hasattr(self, "line2") and self.line2 is not None:
            params['line2'] = self.line2
        if hasattr(self, "postal_code") and self.postal_code is not None:
            params['postalCode'] = self.postal_code
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'country' in response_body:
            self.__country = response_body['country']
        if 'region' in response_body:
            self.__region = response_body['region']
        if 'county' in response_body:
            self.__county = response_body['county']
        if 'city' in response_body:
            self.__city = response_body['city']
        if 'district' in response_body:
            self.__district = response_body['district']
        if 'line1' in response_body:
            self.__line1 = response_body['line1']
        if 'line2' in response_body:
            self.__line2 = response_body['line2']
        if 'postalCode' in response_body:
            self.__postal_code = response_body['postalCode']
