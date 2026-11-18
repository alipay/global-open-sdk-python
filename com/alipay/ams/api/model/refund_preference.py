import json




class RefundPreference:
    def __init__(self):
        
        self.__preference_type = None  # type: str
        

    @property
    def preference_type(self):
        """
        The type of refund preference. NO_PREFERENCE: No preferred currency to receive the refund amount. This currency will be the transaction outflow currency. ORIGINAL_CURRENCY: refund amount will be converted and added to the original balance, which was deducted during the payment.
        """
        return self.__preference_type

    @preference_type.setter
    def preference_type(self, value):
        self.__preference_type = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "preference_type") and self.preference_type is not None:
            params['preferenceType'] = self.preference_type
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'preferenceType' in response_body:
            self.__preference_type = response_body['preferenceType']
