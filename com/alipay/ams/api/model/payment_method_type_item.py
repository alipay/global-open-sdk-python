import json




class PaymentMethodTypeItem:
    def __init__(self):
        
        self.__payment_method_type = None  # type: str
        self.__payment_method_order = None  # type: int
        self.__express_checkout = None  # type: bool
        

    @property
    def payment_method_type(self):
        """
        The payment method type that is included in payment method options. See Payment methods to check the valid values.   More information:  Value range: 64
        """
        return self.__payment_method_type

    @payment_method_type.setter
    def payment_method_type(self, value):
        self.__payment_method_type = value
    @property
    def payment_method_order(self):
        """
        The priority order of the payment methods configured by the user is indicated by numerical values, with smaller numbers representing higher priority. If the user does not specify a setting, Antom will apply a default sorting method.  More information:  Value range: [1, +∞)
        """
        return self.__payment_method_order

    @payment_method_order.setter
    def payment_method_order(self, value):
        self.__payment_method_order = value
    @property
    def express_checkout(self):
        """
        Indicates whether the payment method selected by the user is displayed as a quick payment method. The currently supported quick payment methods include ALIPAY_CN, APPLEPAY, and GOOGLAPAY. The valid values include:  true: The payment method selected by the user is displayed as a quick payment method. false: The payment method selected by the user is not displayed as a quick payment method. 
        """
        return self.__express_checkout

    @express_checkout.setter
    def express_checkout(self, value):
        self.__express_checkout = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "payment_method_type") and self.payment_method_type is not None:
            params['paymentMethodType'] = self.payment_method_type
        if hasattr(self, "payment_method_order") and self.payment_method_order is not None:
            params['paymentMethodOrder'] = self.payment_method_order
        if hasattr(self, "express_checkout") and self.express_checkout is not None:
            params['expressCheckout'] = self.express_checkout
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'paymentMethodType' in response_body:
            self.__payment_method_type = response_body['paymentMethodType']
        if 'paymentMethodOrder' in response_body:
            self.__payment_method_order = response_body['paymentMethodOrder']
        if 'expressCheckout' in response_body:
            self.__express_checkout = response_body['expressCheckout']
