import json




class FundTransferName:
    def __init__(self):
        
        self.__first_name = None  # type: str
        self.__last_name = None  # type: str
        

    @property
    def first_name(self):
        """
        The first (given) name of the fund sender or recipient, collected for AML compliance. Maximum length: 32 characters.
        """
        return self.__first_name

    @first_name.setter
    def first_name(self, value):
        self.__first_name = value
    @property
    def last_name(self):
        """
        The last (family) name of the fund sender or recipient, collected for AML compliance. Maximum length: 32 characters.
        """
        return self.__last_name

    @last_name.setter
    def last_name(self, value):
        self.__last_name = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "first_name") and self.first_name is not None:
            params['firstName'] = self.first_name
        if hasattr(self, "last_name") and self.last_name is not None:
            params['lastName'] = self.last_name
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'firstName' in response_body:
            self.__first_name = response_body['firstName']
        if 'lastName' in response_body:
            self.__last_name = response_body['lastName']
