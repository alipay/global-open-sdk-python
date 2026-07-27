import json



from com.alipay.ams.api.request.alipay_request import AlipayRequest

class AlipayPromotionCodeUpdateRequest(AlipayRequest):
    def __init__(self):
        super(AlipayPromotionCodeUpdateRequest, self).__init__("/ams/api/v1/billing/promotionCode/update") 

        self.__promotion_code_id = None  # type: str
        self.__status = None  # type: str
        self.__max_redemptions = None  # type: int
        self.__expiry_time = None  # type: str
        self.__metadata = None  # type: {str: (str,)}
        

    @property
    def promotion_code_id(self):
        """
        The promotion code ID. Maximum length: 64 characters.
        """
        return self.__promotion_code_id

    @promotion_code_id.setter
    def promotion_code_id(self, value):
        self.__promotion_code_id = value
    @property
    def status(self):
        """
        The current status. Maximum length: 16 characters.
        """
        return self.__status

    @status.setter
    def status(self, value):
        self.__status = value
    @property
    def max_redemptions(self):
        """
        The max redemptions.
        """
        return self.__max_redemptions

    @max_redemptions.setter
    def max_redemptions(self, value):
        self.__max_redemptions = value
    @property
    def expiry_time(self):
        """
        The expiry time.
        """
        return self.__expiry_time

    @expiry_time.setter
    def expiry_time(self, value):
        self.__expiry_time = value
    @property
    def metadata(self):
        """
        Custom metadata for special use cases. Maximum length: 65535 characters.
        """
        return self.__metadata

    @metadata.setter
    def metadata(self, value):
        self.__metadata = value


    def to_ams_json(self): 
        json_str = json.dumps(obj=self.to_ams_dict(), default=lambda o: o.to_ams_dict(), indent=3) 
        return json_str


    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "promotion_code_id") and self.promotion_code_id is not None:
            params['promotionCodeId'] = self.promotion_code_id
        if hasattr(self, "status") and self.status is not None:
            params['status'] = self.status
        if hasattr(self, "max_redemptions") and self.max_redemptions is not None:
            params['maxRedemptions'] = self.max_redemptions
        if hasattr(self, "expiry_time") and self.expiry_time is not None:
            params['expiryTime'] = self.expiry_time
        if hasattr(self, "metadata") and self.metadata is not None:
            params['metadata'] = self.metadata
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'promotionCodeId' in response_body:
            self.__promotion_code_id = response_body['promotionCodeId']
        if 'status' in response_body:
            self.__status = response_body['status']
        if 'maxRedemptions' in response_body:
            self.__max_redemptions = response_body['maxRedemptions']
        if 'expiryTime' in response_body:
            self.__expiry_time = response_body['expiryTime']
        if 'metadata' in response_body:
            self.__metadata = response_body['metadata']
