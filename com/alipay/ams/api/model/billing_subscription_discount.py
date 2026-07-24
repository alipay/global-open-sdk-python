import json




class BillingSubscriptionDiscount:
    def __init__(self):
        
        self.__coupon_id = None  # type: str
        self.__promotion_code_id = None  # type: str
        

    @property
    def coupon_id(self):
        """
        Coupon ID.
        """
        return self.__coupon_id

    @coupon_id.setter
    def coupon_id(self, value):
        self.__coupon_id = value
    @property
    def promotion_code_id(self):
        """
        Promotion code ID.
        """
        return self.__promotion_code_id

    @promotion_code_id.setter
    def promotion_code_id(self, value):
        self.__promotion_code_id = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "coupon_id") and self.coupon_id is not None:
            params['couponId'] = self.coupon_id
        if hasattr(self, "promotion_code_id") and self.promotion_code_id is not None:
            params['promotionCodeId'] = self.promotion_code_id
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'couponId' in response_body:
            self.__coupon_id = response_body['couponId']
        if 'promotionCodeId' in response_body:
            self.__promotion_code_id = response_body['promotionCodeId']
