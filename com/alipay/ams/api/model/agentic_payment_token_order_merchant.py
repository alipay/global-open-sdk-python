import json




class AgenticPaymentTokenOrderMerchant:
    def __init__(self):
        
        self.__reference_merchant_id = None  # type: str
        self.__merchant_name = None  # type: str
        self.__merchant_mcc = None  # type: str
        self.__merchant_url = None  # type: str
        self.__merchant_country_code = None  # type: str
        

    @property
    def reference_merchant_id(self):
        """
        Merchant identifier. Required for A+.
        """
        return self.__reference_merchant_id

    @reference_merchant_id.setter
    def reference_merchant_id(self, value):
        self.__reference_merchant_id = value
    @property
    def merchant_name(self):
        """
        Merchant name. Required for Visa AUTONOMOUS submitted here; Visa IMMEDIATE reuses the previous authorization context.
        """
        return self.__merchant_name

    @merchant_name.setter
    def merchant_name(self, value):
        self.__merchant_name = value
    @property
    def merchant_mcc(self):
        """
        Merchant category code.
        """
        return self.__merchant_mcc

    @merchant_mcc.setter
    def merchant_mcc(self, value):
        self.__merchant_mcc = value
    @property
    def merchant_url(self):
        """
        Merchant website URL (Mastercard payee.website). Required for Visa AUTONOMOUS; Visa IMMEDIATE reuses the authorization context.
        """
        return self.__merchant_url

    @merchant_url.setter
    def merchant_url(self, value):
        self.__merchant_url = value
    @property
    def merchant_country_code(self):
        """
        ISO 3166-1 alpha-2 merchant country or region code. Required for Visa AUTONOMOUS; Visa IMMEDIATE reuses the authorization context.
        """
        return self.__merchant_country_code

    @merchant_country_code.setter
    def merchant_country_code(self, value):
        self.__merchant_country_code = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "reference_merchant_id") and self.reference_merchant_id is not None:
            params['referenceMerchantId'] = self.reference_merchant_id
        if hasattr(self, "merchant_name") and self.merchant_name is not None:
            params['merchantName'] = self.merchant_name
        if hasattr(self, "merchant_mcc") and self.merchant_mcc is not None:
            params['merchantMCC'] = self.merchant_mcc
        if hasattr(self, "merchant_url") and self.merchant_url is not None:
            params['merchantUrl'] = self.merchant_url
        if hasattr(self, "merchant_country_code") and self.merchant_country_code is not None:
            params['merchantCountryCode'] = self.merchant_country_code
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'referenceMerchantId' in response_body:
            self.__reference_merchant_id = response_body['referenceMerchantId']
        if 'merchantName' in response_body:
            self.__merchant_name = response_body['merchantName']
        if 'merchantMCC' in response_body:
            self.__merchant_mcc = response_body['merchantMCC']
        if 'merchantUrl' in response_body:
            self.__merchant_url = response_body['merchantUrl']
        if 'merchantCountryCode' in response_body:
            self.__merchant_country_code = response_body['merchantCountryCode']
