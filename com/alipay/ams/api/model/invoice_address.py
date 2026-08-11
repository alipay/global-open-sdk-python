import json




class InvoiceAddress:
    def __init__(self):
        
        self.__country = None  # type: str
        self.__state = None  # type: str
        self.__city = None  # type: str
        self.__address1 = None  # type: str
        self.__address2 = None  # type: str
        self.__postal_code = None  # type: str
        

    @property
    def country(self):
        """
        Two-letter country code that follows ISO 3166-1 alpha-2. Maximum length: 8 characters.
        """
        return self.__country

    @country.setter
    def country(self, value):
        self.__country = value
    @property
    def state(self):
        """
        State, province, or region. Maximum length: 128 characters.
        """
        return self.__state

    @state.setter
    def state(self, value):
        self.__state = value
    @property
    def city(self):
        """
        City, district, suburb, town, or village. Maximum length: 256 characters.
        """
        return self.__city

    @city.setter
    def city(self, value):
        self.__city = value
    @property
    def address1(self):
        """
        Primary address line. Maximum length: 1024 characters.
        """
        return self.__address1

    @address1.setter
    def address1(self, value):
        self.__address1 = value
    @property
    def address2(self):
        """
        Additional address line. Maximum length: 1024 characters.
        """
        return self.__address2

    @address2.setter
    def address2(self, value):
        self.__address2 = value
    @property
    def postal_code(self):
        """
        Postal or ZIP code. Maximum length: 32 characters.
        """
        return self.__postal_code

    @postal_code.setter
    def postal_code(self, value):
        self.__postal_code = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "country") and self.country is not None:
            params['country'] = self.country
        if hasattr(self, "state") and self.state is not None:
            params['state'] = self.state
        if hasattr(self, "city") and self.city is not None:
            params['city'] = self.city
        if hasattr(self, "address1") and self.address1 is not None:
            params['address1'] = self.address1
        if hasattr(self, "address2") and self.address2 is not None:
            params['address2'] = self.address2
        if hasattr(self, "postal_code") and self.postal_code is not None:
            params['postalCode'] = self.postal_code
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'country' in response_body:
            self.__country = response_body['country']
        if 'state' in response_body:
            self.__state = response_body['state']
        if 'city' in response_body:
            self.__city = response_body['city']
        if 'address1' in response_body:
            self.__address1 = response_body['address1']
        if 'address2' in response_body:
            self.__address2 = response_body['address2']
        if 'postalCode' in response_body:
            self.__postal_code = response_body['postalCode']
