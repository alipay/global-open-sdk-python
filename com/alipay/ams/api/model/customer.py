import json




class Customer:
    def __init__(self):
        
        self.__customer_id = None  # type: str
        self.__customer_request_id = None  # type: str
        self.__email = None  # type: str
        self.__first_name = None  # type: str
        self.__last_name = None  # type: str
        self.__status = None  # type: str
        self.__billing_email = None  # type: str
        self.__country = None  # type: str
        self.__gmt_create = None  # type: str
        

    @property
    def customer_id(self):
        """
        Filter by exact customer ID (single exact match).
        """
        return self.__customer_id

    @customer_id.setter
    def customer_id(self, value):
        self.__customer_id = value
    @property
    def customer_request_id(self):
        """
        Merchant-supplied idempotency key.
        """
        return self.__customer_request_id

    @customer_request_id.setter
    def customer_request_id(self, value):
        self.__customer_request_id = value
    @property
    def email(self):
        """
        Filter by exact email address match. Maximum length: 256 characters.
        """
        return self.__email

    @email.setter
    def email(self, value):
        self.__email = value
    @property
    def first_name(self):
        """
        Customer first name. Returned when the field was set.
        """
        return self.__first_name

    @first_name.setter
    def first_name(self, value):
        self.__first_name = value
    @property
    def last_name(self):
        """
        Customer last name. Returned when the field was set.
        """
        return self.__last_name

    @last_name.setter
    def last_name(self, value):
        self.__last_name = value
    @property
    def status(self):
        """
        Filter by customer status. Allowed values: &#x60;ACTIVE&#x60;, &#x60;DELETED&#x60;. If not provided, returns customers of all statuses.
        """
        return self.__status

    @status.setter
    def status(self, value):
        self.__status = value
    @property
    def billing_email(self):
        """
        Invoice recipient email (independent of account email). Returned when the field was set.
        """
        return self.__billing_email

    @billing_email.setter
    def billing_email(self, value):
        self.__billing_email = value
    @property
    def country(self):
        """
        Filter by billing country codes (ISO 3166-1 alpha-2) using SQL &#x60;IN&#x60; clause. Maximum size: 50 elements.
        """
        return self.__country

    @country.setter
    def country(self, value):
        self.__country = value
    @property
    def gmt_create(self):
        """
        Customer creation timestamp.
        """
        return self.__gmt_create

    @gmt_create.setter
    def gmt_create(self, value):
        self.__gmt_create = value


    

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
        if hasattr(self, "billing_email") and self.billing_email is not None:
            params['billingEmail'] = self.billing_email
        if hasattr(self, "country") and self.country is not None:
            params['country'] = self.country
        if hasattr(self, "gmt_create") and self.gmt_create is not None:
            params['gmtCreate'] = self.gmt_create
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
        if 'billingEmail' in response_body:
            self.__billing_email = response_body['billingEmail']
        if 'country' in response_body:
            self.__country = response_body['country']
        if 'gmtCreate' in response_body:
            self.__gmt_create = response_body['gmtCreate']
