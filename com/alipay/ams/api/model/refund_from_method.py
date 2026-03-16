import json




class RefundFromMethod:
    def __init__(self):
        
        self.__grant_token = None  # type: str
        self.__refund_from_method_type = None  # type: str
        self.__customer_id = None  # type: str
        

    @property
    def grant_token(self):
        """
        Represents the authentication token received from the supplier, used to authorize and securely perform fund deduction operations.
        """
        return self.__grant_token

    @grant_token.setter
    def grant_token(self, value):
        self.__grant_token = value
    @property
    def refund_from_method_type(self):
        """
        Represents the payment method type used by merchant during payment
        """
        return self.__refund_from_method_type

    @refund_from_method_type.setter
    def refund_from_method_type(self, value):
        self.__refund_from_method_type = value
    @property
    def customer_id(self):
        """
        The payee/supplier represented by ABA customer ID to get the refund from
        """
        return self.__customer_id

    @customer_id.setter
    def customer_id(self, value):
        self.__customer_id = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "grant_token") and self.grant_token is not None:
            params['grantToken'] = self.grant_token
        if hasattr(self, "refund_from_method_type") and self.refund_from_method_type is not None:
            params['refundFromMethodType'] = self.refund_from_method_type
        if hasattr(self, "customer_id") and self.customer_id is not None:
            params['customerId'] = self.customer_id
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'grantToken' in response_body:
            self.__grant_token = response_body['grantToken']
        if 'refundFromMethodType' in response_body:
            self.__refund_from_method_type = response_body['refundFromMethodType']
        if 'customerId' in response_body:
            self.__customer_id = response_body['customerId']
