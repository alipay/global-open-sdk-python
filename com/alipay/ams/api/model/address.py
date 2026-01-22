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
        self.__address3 = None  # type: str
        

    @property
    def region(self):
        """
        The 2-letter country or region code. For more information, see the ISO 3166 Country Codes standard.   More information:  Maximum length: 2 characters
        """
        return self.__region

    @region.setter
    def region(self, value):
        self.__region = value
    @property
    def state(self):
        """
        The state, country, or province name.   For card payments, if your business entity is in the United States, and the card issuing country is Canada, the United States, or the United Kingdom, set the value to a region code that consists of two to three characters and follows the ISO 3166-2 standard.   More information:  Maximum length: 8 characters
        """
        return self.__state

    @state.setter
    def state(self, value):
        self.__state = value
    @property
    def city(self):
        """
        The city, district, suburb, town, or village name.   More information:  Maximum length: 32 characters 
        """
        return self.__city

    @city.setter
    def city(self, value):
        self.__city = value
    @property
    def address1(self):
        """
        Address line 1, for example, the street address, PO box, and company name.   More information:  Maximum length: 256 characters
        """
        return self.__address1

    @address1.setter
    def address1(self, value):
        self.__address1 = value
    @property
    def address2(self):
        """
        Address line 2, for example, the apartment, suite, unit, and building information.   More information:  Maximum length: 256 characters
        """
        return self.__address2

    @address2.setter
    def address2(self, value):
        self.__address2 = value
    @property
    def zip_code(self):
        """
        The ZIP or postal code.   For card payments, if your business entity is in the United States, specify this parameter according to the following parameter value requirements:  Only contains numbers, letters, hyphens, and spaces. Must be within ten characters.  More information:  Maximum length: 32 characters
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
    @property
    def address3(self):
        """Gets the address3 of this Address.
        
        """
        return self.__address3

    @address3.setter
    def address3(self, value):
        self.__address3 = value


    

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
        if hasattr(self, "address3") and self.address3 is not None:
            params['address3'] = self.address3
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
        if 'address3' in response_body:
            self.__address3 = response_body['address3']
