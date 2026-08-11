import json



from com.alipay.ams.api.request.alipay_request import AlipayRequest

class AlipayPriceInquireDetailsRequest(AlipayRequest):
    def __init__(self):
        super(AlipayPriceInquireDetailsRequest, self).__init__("/ams/api/v1/billing/price/inquireDetails") 

        self.__price_id = None  # type: str
        

    @property
    def price_id(self):
        """
        Price ID to query. Cannot be null. Format: price_ prefix + alphanumeric suffix. This field serves as the idempotent key for this operation
        """
        return self.__price_id

    @price_id.setter
    def price_id(self, value):
        self.__price_id = value


    def to_ams_json(self): 
        json_str = json.dumps(obj=self.to_ams_dict(), default=lambda o: o.to_ams_dict(), indent=3) 
        return json_str


    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "price_id") and self.price_id is not None:
            params['priceId'] = self.price_id
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'priceId' in response_body:
            self.__price_id = response_body['priceId']
