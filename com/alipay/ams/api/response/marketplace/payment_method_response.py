import json



from com.alipay.ams.api.response.alipay_response import AlipayResponse

class PaymentMethodResponse(AlipayResponse):
    def __init__(self, rsp_body):
        super(AlipayResponse, self).__init__() 

        self.__payment_method_type = None  # type: str
        self.__customer_id = None  # type: str
        self.parse_rsp_body(rsp_body) 


    @property
    def payment_method_type(self):
        """
        The payment method type that is included in payment method options. The value is fixed as: - ANTOM_BIZ_ACCOUNT: Use Antom Biz Account to send or receive funds.
        """
        return self.__payment_method_type

    @payment_method_type.setter
    def payment_method_type(self, value):
        self.__payment_method_type = value
    @property
    def customer_id(self):
        """
        The unique ID to identify a customer.
        """
        return self.__customer_id

    @customer_id.setter
    def customer_id(self, value):
        self.__customer_id = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "payment_method_type") and self.payment_method_type is not None:
            params['paymentMethodType'] = self.payment_method_type
        if hasattr(self, "customer_id") and self.customer_id is not None:
            params['customerId'] = self.customer_id
        return params


    def parse_rsp_body(self, response_body):
        response_body = super(PaymentMethodResponse, self).parse_rsp_body(response_body)
        if 'paymentMethodType' in response_body:
            self.__payment_method_type = response_body['paymentMethodType']
        if 'customerId' in response_body:
            self.__customer_id = response_body['customerId']
