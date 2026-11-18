import json
from com.alipay.ams.api.model.payment_method import PaymentMethod




class PaymentEvaluation:
    def __init__(self):
        
        self.__payment_methods = None  # type: [PaymentMethod]
        

    @property
    def payment_methods(self):
        """Gets the payment_methods of this PaymentEvaluation.
        
        """
        return self.__payment_methods

    @payment_methods.setter
    def payment_methods(self, value):
        self.__payment_methods = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "payment_methods") and self.payment_methods is not None:
            params['paymentMethods'] = self.payment_methods
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'paymentMethods' in response_body:
            self.__payment_methods = []
            for item in response_body['paymentMethods']:
                obj = PaymentMethod()
                obj.parse_rsp_body(item)
                self.__payment_methods.append(obj)
