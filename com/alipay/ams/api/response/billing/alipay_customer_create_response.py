import json
from com.alipay.ams.api.model.result import Result



from com.alipay.ams.api.response.alipay_response import AlipayResponse

class AlipayCustomerCreateResponse(AlipayResponse):
    def __init__(self, rsp_body):
        super(AlipayResponse, self).__init__() 

        self.__result = None  # type: Result
        self.__customer_id = None  # type: str
        self.__customer_request_id = None  # type: str
        self.__email = None  # type: str
        self.__status = None  # type: str
        self.__phone_no = None  # type: str
        self.__country_code = None  # type: str
        self.__billing_email = None  # type: str
        self.__shipping_first_name = None  # type: str
        self.__shipping_last_name = None  # type: str
        self.__shipping_country_code = None  # type: str
        self.parse_rsp_body(rsp_body) 


    @property
    def result(self):
        """Gets the result of this AlipayCustomerCreateResponse.
        
        """
        return self.__result

    @result.setter
    def result(self, value):
        self.__result = value
    @property
    def customer_id(self):
        """
        The unique ID assigned by Antom to identify a customer. Maximum length: 64 characters. Note: See documentation for details.
        """
        return self.__customer_id

    @customer_id.setter
    def customer_id(self, value):
        self.__customer_id = value
    @property
    def customer_request_id(self):
        """
        The unique ID assigned by a merchant to identify a request. Maximum length: 64 characters. Note: See documentation for details.
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
    def status(self):
        """
        The current status. Maximum length: 16 characters. Note: See documentation for details.
        """
        return self.__status

    @status.setter
    def status(self, value):
        self.__status = value
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
        if hasattr(self, "customer_id") and self.customer_id is not None:
            params['customerId'] = self.customer_id
        if hasattr(self, "customer_request_id") and self.customer_request_id is not None:
            params['customerRequestId'] = self.customer_request_id
        if hasattr(self, "email") and self.email is not None:
            params['email'] = self.email
        if hasattr(self, "status") and self.status is not None:
            params['status'] = self.status
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
        response_body = super(AlipayCustomerCreateResponse, self).parse_rsp_body(response_body)
        if 'result' in response_body:
            self.__result = Result()
            self.__result.parse_rsp_body(response_body['result'])
        if 'customerId' in response_body:
            self.__customer_id = response_body['customerId']
        if 'customerRequestId' in response_body:
            self.__customer_request_id = response_body['customerRequestId']
        if 'email' in response_body:
            self.__email = response_body['email']
        if 'status' in response_body:
            self.__status = response_body['status']
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
