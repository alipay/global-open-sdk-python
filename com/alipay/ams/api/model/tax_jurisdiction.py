import json




class TaxJurisdiction:
    def __init__(self):
        
        self.__country = None  # type: str
        self.__region = None  # type: str
        self.__county = None  # type: str
        self.__city = None  # type: str
        self.__district = None  # type: str
        

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
