import json




class UserName:
    def __init__(self):
        
        self.__first_name = None  # type: str
        self.__middle_name = None  # type: str
        self.__last_name = None  # type: str
        self.__full_name = None  # type: str
        

    @property
    def first_name(self):
        """
        First name.  More information:  Maximum length: 32 characters
        """
        return self.__first_name

    @first_name.setter
    def first_name(self, value):
        self.__first_name = value
    @property
    def middle_name(self):
        """
        Middle name  More information:  Maximum length: 32 characters
        """
        return self.__middle_name

    @middle_name.setter
    def middle_name(self, value):
        self.__middle_name = value
    @property
    def last_name(self):
        """
        Last name  More information:  Maximum length: 32 characters
        """
        return self.__last_name

    @last_name.setter
    def last_name(self, value):
        self.__last_name = value
    @property
    def full_name(self):
        """
        Full name  More information:  Maximum length: 128 characters
        """
        return self.__full_name

    @full_name.setter
    def full_name(self, value):
        self.__full_name = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "first_name") and self.first_name is not None:
            params['firstName'] = self.first_name
        if hasattr(self, "middle_name") and self.middle_name is not None:
            params['middleName'] = self.middle_name
        if hasattr(self, "last_name") and self.last_name is not None:
            params['lastName'] = self.last_name
        if hasattr(self, "full_name") and self.full_name is not None:
            params['fullName'] = self.full_name
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'firstName' in response_body:
            self.__first_name = response_body['firstName']
        if 'middleName' in response_body:
            self.__middle_name = response_body['middleName']
        if 'lastName' in response_body:
            self.__last_name = response_body['lastName']
        if 'fullName' in response_body:
            self.__full_name = response_body['fullName']
