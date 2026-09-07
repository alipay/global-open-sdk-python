import json




class AccountLastModified:
    def __init__(self):
        
        self.__password_change_date = None  # type: str
        self.__email_change_date = None  # type: str
        self.__listing_change_date = None  # type: str
        self.__login_date = None  # type: str
        self.__address_change_date = None  # type: str
        

    @property
    def password_change_date(self):
        """
        The date and time when the merchant last changed the account password. The value follows the ISO 8601 standard format. For example, \&quot;2019-11-27T12:01:01+08:00\&quot;.
        """
        return self.__password_change_date

    @password_change_date.setter
    def password_change_date(self, value):
        self.__password_change_date = value
    @property
    def email_change_date(self):
        """
        The date and time when the merchant last changed the account email address. The value follows the ISO 8601 standard format. For example, \&quot;2019-11-27T12:01:01+08:00\&quot;.
        """
        return self.__email_change_date

    @email_change_date.setter
    def email_change_date(self, value):
        self.__email_change_date = value
    @property
    def listing_change_date(self):
        """
        The date and time when the merchant last changed the account listing information. The value follows the ISO 8601 standard format. For example, \&quot;2019-11-27T12:01:01+08:00\&quot;.
        """
        return self.__listing_change_date

    @listing_change_date.setter
    def listing_change_date(self, value):
        self.__listing_change_date = value
    @property
    def login_date(self):
        """
        The date and time when the merchant last logged in to the account. The value follows the ISO 8601 standard format. For example, \&quot;2019-11-27T12:01:01+08:00\&quot;.
        """
        return self.__login_date

    @login_date.setter
    def login_date(self, value):
        self.__login_date = value
    @property
    def address_change_date(self):
        """
        The date and time when the merchant last changed the account address. The value follows the ISO 8601 standard format. For example, \&quot;2019-11-27T12:01:01+08:00\&quot;.
        """
        return self.__address_change_date

    @address_change_date.setter
    def address_change_date(self, value):
        self.__address_change_date = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "password_change_date") and self.password_change_date is not None:
            params['passwordChangeDate'] = self.password_change_date
        if hasattr(self, "email_change_date") and self.email_change_date is not None:
            params['emailChangeDate'] = self.email_change_date
        if hasattr(self, "listing_change_date") and self.listing_change_date is not None:
            params['listingChangeDate'] = self.listing_change_date
        if hasattr(self, "login_date") and self.login_date is not None:
            params['loginDate'] = self.login_date
        if hasattr(self, "address_change_date") and self.address_change_date is not None:
            params['addressChangeDate'] = self.address_change_date
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'passwordChangeDate' in response_body:
            self.__password_change_date = response_body['passwordChangeDate']
        if 'emailChangeDate' in response_body:
            self.__email_change_date = response_body['emailChangeDate']
        if 'listingChangeDate' in response_body:
            self.__listing_change_date = response_body['listingChangeDate']
        if 'loginDate' in response_body:
            self.__login_date = response_body['loginDate']
        if 'addressChangeDate' in response_body:
            self.__address_change_date = response_body['addressChangeDate']
