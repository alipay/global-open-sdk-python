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
        System-generated unique customer ID. Returned when resultCode is &#x60;SUCCESS&#x60;.
        """
        return self.__customer_id

    @customer_id.setter
    def customer_id(self, value):
        self.__customer_id = value
    @property
    def customer_request_id(self):
        """
        Echo of the merchant-supplied idempotency key. Returned when resultCode is &#x60;SUCCESS&#x60;.
        """
        return self.__customer_request_id

    @customer_request_id.setter
    def customer_request_id(self, value):
        self.__customer_request_id = value
    @property
    def email(self):
        """
        Email address recorded for this customer. Returned when resultCode is &#x60;SUCCESS&#x60; and email was provided at creation.
        """
        return self.__email

    @email.setter
    def email(self, value):
        self.__email = value
    @property
    def status(self):
        """
        Customer status. Value: &#x60;ACTIVE&#x60;. Returned when resultCode is &#x60;SUCCESS&#x60;.
        """
        return self.__status

    @status.setter
    def status(self, value):
        self.__status = value


    

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
