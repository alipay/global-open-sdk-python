import json




class AgenticBoundPaymentMethodDetail:
    def __init__(self):
        
        self.__card_brand = None  # type: str
        self.__last_four = None  # type: str
        

    @property
    def card_brand(self):
        """
        Controlled card-brand display value. Required for CARD; the closed, case-sensitive values are VISA and MASTERCARD. Other card brands are excluded from paymentMethods. APM wallet names are returned in paymentMethodType. Supported values (case-sensitive): VISA, MASTERCARD.
        """
        return self.__card_brand

    @card_brand.setter
    def card_brand(self, value):
        self.__card_brand = value
    @property
    def last_four(self):
        """
        Masked last-four-character summary of the payment asset or account. Returned for CARD and the currently supported APM wallets.
        """
        return self.__last_four

    @last_four.setter
    def last_four(self, value):
        self.__last_four = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "card_brand") and self.card_brand is not None:
            params['cardBrand'] = self.card_brand
        if hasattr(self, "last_four") and self.last_four is not None:
            params['lastFour'] = self.last_four
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'cardBrand' in response_body:
            self.__card_brand = response_body['cardBrand']
        if 'lastFour' in response_body:
            self.__last_four = response_body['lastFour']
