import json




class Customer:
    def __init__(self):
        
        self.__customer_id = None  # type: str
        self.__customer_request_id = None  # type: str
        self.__email = None  # type: str
        self.__first_name = None  # type: str
        self.__last_name = None  # type: str
        self.__status = None  # type: str
        

    @property
    def customer_id(self):
        """
        The unique ID assigned by Antom to identify a customer. Maximum length: 64 characters.
        """
        return self.__customer_id

    @customer_id.setter
    def customer_id(self, value):
        self.__customer_id = value
    @property
    def customer_request_id(self):
        """
        The unique ID assigned by a merchant to identify a request. Maximum length: 64 characters.
        """
        return self.__customer_request_id

    @customer_request_id.setter
    def customer_request_id(self, value):
        self.__customer_request_id = value
    @property
    def email(self):
        """
        The email address. Maximum length: 256 characters. Note: See documentation for details.
        """
        return self.__email

    @email.setter
    def email(self, value):
        self.__email = value
    @property
    def first_name(self):
        """
        The first name. Maximum length: 256 characters. Note: See documentation for details.
        """
        return self.__first_name

    @first_name.setter
    def first_name(self, value):
        self.__first_name = value
    @property
    def last_name(self):
        """
        The last name. Maximum length: 256 characters. Note: See documentation for details.
        """
        return self.__last_name

    @last_name.setter
    def last_name(self, value):
        self.__last_name = value
    @property
    def status(self):
        """
        The current status. Maximum length: 16 characters.
        """
        return self.__status

    @status.setter
    def status(self, value):
        self.__status = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "customer_id") and self.customer_id is not None:
            params['customerId'] = self.customer_id
        if hasattr(self, "customer_request_id") and self.customer_request_id is not None:
            params['customerRequestId'] = self.customer_request_id
        if hasattr(self, "email") and self.email is not None:
            params['email'] = self.email
        if hasattr(self, "first_name") and self.first_name is not None:
            params['firstName'] = self.first_name
        if hasattr(self, "last_name") and self.last_name is not None:
            params['lastName'] = self.last_name
        if hasattr(self, "status") and self.status is not None:
            params['status'] = self.status
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'customerId' in response_body:
            self.__customer_id = response_body['customerId']
        if 'customerRequestId' in response_body:
            self.__customer_request_id = response_body['customerRequestId']
        if 'email' in response_body:
            self.__email = response_body['email']
        if 'firstName' in response_body:
            self.__first_name = response_body['firstName']
        if 'lastName' in response_body:
            self.__last_name = response_body['lastName']
        if 'status' in response_body:
            self.__status = response_body['status']
