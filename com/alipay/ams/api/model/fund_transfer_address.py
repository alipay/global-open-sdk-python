import json




class FundTransferAddress:
    def __init__(self):
        
        self.__address1 = None  # type: str
        self.__city = None  # type: str
        self.__state = None  # type: str
        self.__region = None  # type: str
        

    @property
    def address1(self):
        """
        Street address of the fund transfer party. Maximum length: 256 characters.
        """
        return self.__address1

    @address1.setter
    def address1(self, value):
        self.__address1 = value
    @property
    def city(self):
        """
        City of the fund transfer party. Maximum length: 32 characters.
        """
        return self.__city

    @city.setter
    def city(self, value):
        self.__city = value
    @property
    def state(self):
        """
        State, province, or administrative division code of the fund transfer party. Maximum length: 64 characters.
        """
        return self.__state

    @state.setter
    def state(self, value):
        self.__state = value
    @property
    def region(self):
        """
        Two-letter country code of the fund transfer party in ISO 3166-1 alpha-2 format. Maximum length: 2 characters.
        """
        return self.__region

    @region.setter
    def region(self, value):
        self.__region = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "address1") and self.address1 is not None:
            params['address1'] = self.address1
        if hasattr(self, "city") and self.city is not None:
            params['city'] = self.city
        if hasattr(self, "state") and self.state is not None:
            params['state'] = self.state
        if hasattr(self, "region") and self.region is not None:
            params['region'] = self.region
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'address1' in response_body:
            self.__address1 = response_body['address1']
        if 'city' in response_body:
            self.__city = response_body['city']
        if 'state' in response_body:
            self.__state = response_body['state']
        if 'region' in response_body:
            self.__region = response_body['region']
