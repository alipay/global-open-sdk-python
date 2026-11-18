import json




class ReceiptPaymentMethod:
    def __init__(self):
        
        self.__payment_method_type = None  # type: str
        

    @property
    def payment_method_type(self):
        """
        The payment method type, such as CARD.
        """
        return self.__payment_method_type

    @payment_method_type.setter
    def payment_method_type(self, value):
        self.__payment_method_type = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "payment_method_type") and self.payment_method_type is not None:
            params['paymentMethodType'] = self.payment_method_type
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'paymentMethodType' in response_body:
            self.__payment_method_type = response_body['paymentMethodType']
