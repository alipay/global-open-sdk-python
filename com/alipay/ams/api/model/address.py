import json




class Address:
    def __init__(self):
        
        self.__region = None  # type: str
        self.__state = None  # type: str
        self.__city = None  # type: str
        self.__address1 = None  # type: str
        self.__address2 = None  # type: str
        self.__zip_code = None  # type: str
        self.__label = None  # type: str
        

    @property
    def region(self):
        """Gets the region of this Address.
        
        """
        return self.__region

    @region.setter
    def region(self, value):
        self.__region = value
    @property
    def state(self):
        """Gets the state of this Address.
        
        """
        return self.__state

    @state.setter
    def state(self, value):
        self.__state = value
    @property
    def city(self):
        """Gets the city of this Address.
        
        """
        return self.__city

    @city.setter
    def city(self, value):
        self.__city = value
    @property
    def address1(self):
        """Gets the address1 of this Address.
        
        """
        return self.__address1

    @address1.setter
    def address1(self, value):
        self.__address1 = value
    @property
    def address2(self):
        """Gets the address2 of this Address.
        
        """
        return self.__address2

    @address2.setter
    def address2(self, value):
        self.__address2 = value
    @property
    def zip_code(self):
        """Gets the zip_code of this Address.
        
        """
        return self.__zip_code

    @zip_code.setter
    def zip_code(self, value):
        self.__zip_code = value
    @property
    def label(self):
        """Gets the label of this Address.
        
        """
        return self.__label

    @label.setter
    def label(self, value):
        self.__label = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "region") and self.region is not None:
            params['region'] = self.region
        if hasattr(self, "state") and self.state is not None:
            params['state'] = self.state
        if hasattr(self, "city") and self.city is not None:
            params['city'] = self.city
        if hasattr(self, "address1") and self.address1 is not None:
            params['address1'] = self.address1
        if hasattr(self, "address2") and self.address2 is not None:
            params['address2'] = self.address2
        if hasattr(self, "zip_code") and self.zip_code is not None:
            params['zipCode'] = self.zip_code
        if hasattr(self, "label") and self.label is not None:
            params['label'] = self.label
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'region' in response_body:
            self.__region = response_body['region']
        if 'state' in response_body:
            self.__state = response_body['state']
        if 'city' in response_body:
            self.__city = response_body['city']
        if 'address1' in response_body:
            self.__address1 = response_body['address1']
        if 'address2' in response_body:
            self.__address2 = response_body['address2']
        if 'zipCode' in response_body:
            self.__zip_code = response_body['zipCode']
        if 'label' in response_body:
            self.__label = response_body['label']
