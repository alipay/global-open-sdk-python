import json



from com.alipay.ams.api.request.alipay_request import AlipayRequest

class AlipayCouponInquireDetailsRequest(AlipayRequest):
    def __init__(self):
        super(AlipayCouponInquireDetailsRequest, self).__init__("/ams/api/v1/billing/coupon/inquireDetails") 

        self.__coupon_id = None  # type: str
        

    @property
    def coupon_id(self):
        """
        The coupon ID. Maximum length: 64 characters.
        """
        return self.__coupon_id

    @coupon_id.setter
    def coupon_id(self, value):
        self.__coupon_id = value


    def to_ams_json(self): 
        json_str = json.dumps(obj=self.to_ams_dict(), default=lambda o: o.to_ams_dict(), indent=3) 
        return json_str


    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "coupon_id") and self.coupon_id is not None:
            params['couponId'] = self.coupon_id
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'couponId' in response_body:
            self.__coupon_id = response_body['couponId']
