import json



from com.alipay.ams.api.request.alipay_request import AlipayRequest

class AlipayProductInquireDetailsRequest(AlipayRequest):
    def __init__(self):
        super(AlipayProductInquireDetailsRequest, self).__init__("/ams/api/v1/billing/product/inquireDetails") 

        self.__product_id = None  # type: str
        self.__include_prices = None  # type: bool
        

    @property
    def product_id(self):
        """
        The product ID. Maximum length: 32 characters.
        """
        return self.__product_id

    @product_id.setter
    def product_id(self, value):
        self.__product_id = value
    @property
    def include_prices(self):
        """
        The include prices.
        """
        return self.__include_prices

    @include_prices.setter
    def include_prices(self, value):
        self.__include_prices = value


    def to_ams_json(self): 
        json_str = json.dumps(obj=self.to_ams_dict(), default=lambda o: o.to_ams_dict(), indent=3) 
        return json_str


    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "product_id") and self.product_id is not None:
            params['productId'] = self.product_id
        if hasattr(self, "include_prices") and self.include_prices is not None:
            params['includePrices'] = self.include_prices
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'productId' in response_body:
            self.__product_id = response_body['productId']
        if 'includePrices' in response_body:
            self.__include_prices = response_body['includePrices']
