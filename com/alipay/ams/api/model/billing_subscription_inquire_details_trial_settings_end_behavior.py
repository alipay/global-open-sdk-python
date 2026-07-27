import json




class BillingSubscriptionInquireDetailsTrialSettingsEndBehavior:
    def __init__(self):
        
        self.__missing_payment_method = None  # type: str
        

    @property
    def missing_payment_method(self):
        """
        The missing payment method. Maximum length: 14 characters.
        """
        return self.__missing_payment_method

    @missing_payment_method.setter
    def missing_payment_method(self, value):
        self.__missing_payment_method = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "missing_payment_method") and self.missing_payment_method is not None:
            params['missingPaymentMethod'] = self.missing_payment_method
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'missingPaymentMethod' in response_body:
            self.__missing_payment_method = response_body['missingPaymentMethod']
