import json
from com.alipay.ams.api.model.result import Result
from com.alipay.ams.api.model.customer import Customer



from com.alipay.ams.api.response.alipay_response import AlipayResponse

class AlipayCustomerInquireListResponse(AlipayResponse):
    def __init__(self, rsp_body):
        super(AlipayResponse, self).__init__() 

        self.__result = None  # type: Result
        self.__customers = None  # type: [Customer]
        self.__total = None  # type: int
        self.__has_more = None  # type: bool
        self.__next_cursor = None  # type: str
        self.__phone_no = None  # type: str
        self.__country_code = None  # type: str
        self.__billing_email = None  # type: str
        self.__shipping_first_name = None  # type: str
        self.__shipping_last_name = None  # type: str
        self.__shipping_country_code = None  # type: str
        self.parse_rsp_body(rsp_body) 


    @property
    def result(self):
        """Gets the result of this AlipayCustomerInquireListResponse.
        
        """
        return self.__result

    @result.setter
    def result(self, value):
        self.__result = value
    @property
    def customers(self):
        """
        The customers. Note: See documentation for details.
        """
        return self.__customers

    @customers.setter
    def customers(self, value):
        self.__customers = value
    @property
    def total(self):
        """
        The total. Note: See documentation for details.
        """
        return self.__total

    @total.setter
    def total(self, value):
        self.__total = value
    @property
    def has_more(self):
        """
        The has more. Note: See documentation for details.
        """
        return self.__has_more

    @has_more.setter
    def has_more(self, value):
        self.__has_more = value
    @property
    def next_cursor(self):
        """
        The next cursor. Maximum length: 64 characters. Note: See documentation for details.
        """
        return self.__next_cursor

    @next_cursor.setter
    def next_cursor(self, value):
        self.__next_cursor = value
    @property
    def phone_no(self):
        """
        The customer&#39;s phone number (digits only). Replaces deprecated mobileNo. Maximum length: 32 characters.
        """
        return self.__phone_no

    @phone_no.setter
    def phone_no(self, value):
        self.__phone_no = value
    @property
    def country_code(self):
        """
        ISO 3166-1 alpha-2 country code paired with phoneNo. Required when phoneNo is provided. Maximum length: 2 characters.
        """
        return self.__country_code

    @country_code.setter
    def country_code(self, value):
        self.__country_code = value
    @property
    def billing_email(self):
        """
        Invoice recipient email address (independent of account email). Maximum length: 256 characters.
        """
        return self.__billing_email

    @billing_email.setter
    def billing_email(self, value):
        self.__billing_email = value
    @property
    def shipping_first_name(self):
        """
        Shipping recipient first name. Replaces deprecated shippingName. Maximum length: 256 characters.
        """
        return self.__shipping_first_name

    @shipping_first_name.setter
    def shipping_first_name(self, value):
        self.__shipping_first_name = value
    @property
    def shipping_last_name(self):
        """
        Shipping recipient last name. Replaces deprecated shippingName. Maximum length: 256 characters.
        """
        return self.__shipping_last_name

    @shipping_last_name.setter
    def shipping_last_name(self, value):
        self.__shipping_last_name = value
    @property
    def shipping_country_code(self):
        """
        ISO 3166-1 alpha-2 country code paired with shippingPhone. Maximum length: 8 characters.
        """
        return self.__shipping_country_code

    @shipping_country_code.setter
    def shipping_country_code(self, value):
        self.__shipping_country_code = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "result") and self.result is not None:
            params['result'] = self.result
        if hasattr(self, "customers") and self.customers is not None:
            params['customers'] = self.customers
        if hasattr(self, "total") and self.total is not None:
            params['total'] = self.total
        if hasattr(self, "has_more") and self.has_more is not None:
            params['hasMore'] = self.has_more
        if hasattr(self, "next_cursor") and self.next_cursor is not None:
            params['nextCursor'] = self.next_cursor
        if hasattr(self, "phone_no") and self.phone_no is not None:
            params['phoneNo'] = self.phone_no
        if hasattr(self, "country_code") and self.country_code is not None:
            params['countryCode'] = self.country_code
        if hasattr(self, "billing_email") and self.billing_email is not None:
            params['billingEmail'] = self.billing_email
        if hasattr(self, "shipping_first_name") and self.shipping_first_name is not None:
            params['shippingFirstName'] = self.shipping_first_name
        if hasattr(self, "shipping_last_name") and self.shipping_last_name is not None:
            params['shippingLastName'] = self.shipping_last_name
        if hasattr(self, "shipping_country_code") and self.shipping_country_code is not None:
            params['shippingCountryCode'] = self.shipping_country_code
        return params


    def parse_rsp_body(self, response_body):
        response_body = super(AlipayCustomerInquireListResponse, self).parse_rsp_body(response_body)
        if 'result' in response_body:
            self.__result = Result()
            self.__result.parse_rsp_body(response_body['result'])
        if 'customers' in response_body:
            self.__customers = []
            for item in response_body['customers']:
                obj = Customer()
                obj.parse_rsp_body(item)
                self.__customers.append(obj)
        if 'total' in response_body:
            self.__total = response_body['total']
        if 'hasMore' in response_body:
            self.__has_more = response_body['hasMore']
        if 'nextCursor' in response_body:
            self.__next_cursor = response_body['nextCursor']
        if 'phoneNo' in response_body:
            self.__phone_no = response_body['phoneNo']
        if 'countryCode' in response_body:
            self.__country_code = response_body['countryCode']
        if 'billingEmail' in response_body:
            self.__billing_email = response_body['billingEmail']
        if 'shippingFirstName' in response_body:
            self.__shipping_first_name = response_body['shippingFirstName']
        if 'shippingLastName' in response_body:
            self.__shipping_last_name = response_body['shippingLastName']
        if 'shippingCountryCode' in response_body:
            self.__shipping_country_code = response_body['shippingCountryCode']
