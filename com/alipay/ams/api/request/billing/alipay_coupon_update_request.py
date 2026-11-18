import json



from com.alipay.ams.api.request.alipay_request import AlipayRequest

class AlipayCouponUpdateRequest(AlipayRequest):
    def __init__(self):
        super(AlipayCouponUpdateRequest, self).__init__("/ams/api/v1/billing/coupon/update") 

        self.__coupon_id = None  # type: str
        self.__coupon_name = None  # type: str
        self.__status = None  # type: str
        self.__redeem_by = None  # type: str
        self.__metadata = None  # type: str
        self.__max_redemptions = None  # type: int
        

    @property
    def coupon_id(self):
        """
        System-generated coupon ID to update. Cannot be empty.
        """
        return self.__coupon_id

    @coupon_id.setter
    def coupon_id(self, value):
        self.__coupon_id = value
    @property
    def coupon_name(self):
        """
        Updated display name. Maximum length: 128 characters.
        """
        return self.__coupon_name

    @coupon_name.setter
    def coupon_name(self, value):
        self.__coupon_name = value
    @property
    def status(self):
        """
        Status transition. Accepted values: &#x60;ACTIVE&#x60; / &#x60;INACTIVE&#x60;. Drives an ACTIVE &lt;-&gt; INACTIVE state change. When null/blank, status is left unchanged. &#x60;EXPIRED&#x60; is system-derived and cannot be set via this API - passing &#x60;EXPIRED&#x60; returns &#x60;PARAM_ILLEGAL&#x60;.
        """
        return self.__status

    @status.setter
    def status(self, value):
        self.__status = value
    @property
    def redeem_by(self):
        """
        Updated redemption expiry time (UTC, ISO 8601). The new deadline must not be earlier than the current &#x60;redeemBy&#x60; - shortening is rejected with &#x60;PARAM_ILLEGAL&#x60;.
        """
        return self.__redeem_by

    @redeem_by.setter
    def redeem_by(self, value):
        self.__redeem_by = value
    @property
    def metadata(self):
        """
        Updated merchant-defined key-value pairs. Full replacement semantics: the entire metadata object is replaced. The value must be a valid JSON object string.
        """
        return self.__metadata

    @metadata.setter
    def metadata(self, value):
        self.__metadata = value
    @property
    def max_redemptions(self):
        """
        Updated maximum redemption count. The new value must be greater than or equal to the number of times already redeemed (&#x60;redeemedCount&#x60;).
        """
        return self.__max_redemptions

    @max_redemptions.setter
    def max_redemptions(self, value):
        self.__max_redemptions = value


    def to_ams_json(self): 
        json_str = json.dumps(obj=self.to_ams_dict(), default=lambda o: o.to_ams_dict(), indent=3) 
        return json_str


    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "coupon_id") and self.coupon_id is not None:
            params['couponId'] = self.coupon_id
        if hasattr(self, "coupon_name") and self.coupon_name is not None:
            params['couponName'] = self.coupon_name
        if hasattr(self, "status") and self.status is not None:
            params['status'] = self.status
        if hasattr(self, "redeem_by") and self.redeem_by is not None:
            params['redeemBy'] = self.redeem_by
        if hasattr(self, "metadata") and self.metadata is not None:
            params['metadata'] = self.metadata
        if hasattr(self, "max_redemptions") and self.max_redemptions is not None:
            params['maxRedemptions'] = self.max_redemptions
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'couponId' in response_body:
            self.__coupon_id = response_body['couponId']
        if 'couponName' in response_body:
            self.__coupon_name = response_body['couponName']
        if 'status' in response_body:
            self.__status = response_body['status']
        if 'redeemBy' in response_body:
            self.__redeem_by = response_body['redeemBy']
        if 'metadata' in response_body:
            self.__metadata = response_body['metadata']
        if 'maxRedemptions' in response_body:
            self.__max_redemptions = response_body['maxRedemptions']
