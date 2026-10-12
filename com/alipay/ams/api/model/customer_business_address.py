import json




class CustomerBusinessAddress:
    def __init__(self):
        
        self.__country = None  # type: str
        self.__state = None  # type: str
        self.__city = None  # type: str
        self.__address = None  # type: str
        self.__zipcode = None  # type: str
        

    @property
    def country(self):
        """
        ISO 3166-1 alpha-2 country code.
        """
        return self.__country

    @country.setter
    def country(self, value):
        self.__country = value
    @property
    def state(self):
        """
        State or province code.
        """
        return self.__state

    @state.setter
    def state(self, value):
        self.__state = value
    @property
    def city(self):
        """
        City name.
        """
        return self.__city

    @city.setter
    def city(self, value):
        self.__city = value
    @property
    def address(self):
        """
        Street address.
        """
        return self.__address

    @address.setter
    def address(self, value):
        self.__address = value
    @property
    def zipcode(self):
        """
        Postal or ZIP code.
        """
        return self.__zipcode

    @zipcode.setter
    def zipcode(self, value):
        self.__zipcode = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "country") and self.country is not None:
            params['country'] = self.country
        if hasattr(self, "state") and self.state is not None:
            params['state'] = self.state
        if hasattr(self, "city") and self.city is not None:
            params['city'] = self.city
        if hasattr(self, "address") and self.address is not None:
            params['address'] = self.address
        if hasattr(self, "zipcode") and self.zipcode is not None:
            params['zipcode'] = self.zipcode
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
        if 'address' in response_body:
            self.__address = response_body['address']
        if 'zipcode' in response_body:
            self.__zipcode = response_body['zipcode']
