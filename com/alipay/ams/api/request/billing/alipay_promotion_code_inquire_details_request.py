import json



from com.alipay.ams.api.request.alipay_request import AlipayRequest

class AlipayPromotionCodeInquireDetailsRequest(AlipayRequest):
    def __init__(self):
        super(AlipayPromotionCodeInquireDetailsRequest, self).__init__("/ams/api/v1/billing/promotionCode/inquireDetails") 

        self.__promotion_code_id = None  # type: str
        

    @property
    def promotion_code_id(self):
        """
        System-generated promotion code ID to query. Cannot be empty. Maximum length: 64 characters.
        """
        return self.__promotion_code_id

    @promotion_code_id.setter
    def promotion_code_id(self, value):
        self.__promotion_code_id = value


    def to_ams_json(self): 
        json_str = json.dumps(obj=self.to_ams_dict(), default=lambda o: o.to_ams_dict(), indent=3) 
        return json_str


    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "promotion_code_id") and self.promotion_code_id is not None:
            params['promotionCodeId'] = self.promotion_code_id
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'promotionCodeId' in response_body:
            self.__promotion_code_id = response_body['promotionCodeId']
