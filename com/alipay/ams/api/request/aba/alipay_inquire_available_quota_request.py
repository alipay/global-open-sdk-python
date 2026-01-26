import json



from com.alipay.ams.api.request.alipay_request import AlipayRequest

class AlipayInquireAvailableQuotaRequest(AlipayRequest):
    def __init__(self):
        super(AlipayInquireAvailableQuotaRequest, self).__init__("/ams/v1/aba/account/inquireAvailableQuota") 

        self.__currency = None  # type: str
        

    @property
    def currency(self):
        """
        currency which we need to query available quota
        """
        return self.__currency

    @currency.setter
    def currency(self, value):
        self.__currency = value


    def to_ams_json(self): 
        json_str = json.dumps(obj=self.to_ams_dict(), default=lambda o: o.to_ams_dict(), indent=3) 
        return json_str


    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "currency") and self.currency is not None:
            params['currency'] = self.currency
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'currency' in response_body:
            self.__currency = response_body['currency']
