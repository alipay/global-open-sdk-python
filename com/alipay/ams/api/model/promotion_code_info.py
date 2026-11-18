import json




class PromotionCodeInfo:
    def __init__(self):
        
        self.__promotion_code_id = None  # type: str
        self.__code = None  # type: str
        self.__status = None  # type: str
        self.__max_redemptions = None  # type: int
        self.__redeemed_count = None  # type: int
        self.__expiry_time = None  # type: str
        self.__create_time = None  # type: str
        

    @property
    def promotion_code_id(self):
        """
        System-generated promotion code ID.
        """
        return self.__promotion_code_id

    @promotion_code_id.setter
    def promotion_code_id(self, value):
        self.__promotion_code_id = value
    @property
    def code(self):
        """
        The promotion code string.
        """
        return self.__code

    @code.setter
    def code(self, value):
        self.__code = value
    @property
    def status(self):
        """
        Filter by promotion code status. Allowed values: &#x60;ACTIVE&#x60;, &#x60;INACTIVE&#x60;. If not provided, returns all statuses.
        """
        return self.__status

    @status.setter
    def status(self, value):
        self.__status = value
    @property
    def max_redemptions(self):
        """
        Maximum redemption count. Value range: 0-999999.
        """
        return self.__max_redemptions

    @max_redemptions.setter
    def max_redemptions(self, value):
        self.__max_redemptions = value
    @property
    def redeemed_count(self):
        """
        Number of times redeemed. Value range: 0-999999.
        """
        return self.__redeemed_count

    @redeemed_count.setter
    def redeemed_count(self, value):
        self.__redeemed_count = value
    @property
    def expiry_time(self):
        """
        Expiry time. Returned when the field was set.
        """
        return self.__expiry_time

    @expiry_time.setter
    def expiry_time(self, value):
        self.__expiry_time = value
    @property
    def create_time(self):
        """
        Creation time (UTC, ISO 8601).
        """
        return self.__create_time

    @create_time.setter
    def create_time(self, value):
        self.__create_time = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "promotion_code_id") and self.promotion_code_id is not None:
            params['promotionCodeId'] = self.promotion_code_id
        if hasattr(self, "code") and self.code is not None:
            params['code'] = self.code
        if hasattr(self, "status") and self.status is not None:
            params['status'] = self.status
        if hasattr(self, "max_redemptions") and self.max_redemptions is not None:
            params['maxRedemptions'] = self.max_redemptions
        if hasattr(self, "redeemed_count") and self.redeemed_count is not None:
            params['redeemedCount'] = self.redeemed_count
        if hasattr(self, "expiry_time") and self.expiry_time is not None:
            params['expiryTime'] = self.expiry_time
        if hasattr(self, "create_time") and self.create_time is not None:
            params['createTime'] = self.create_time
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'promotionCodeId' in response_body:
            self.__promotion_code_id = response_body['promotionCodeId']
        if 'code' in response_body:
            self.__code = response_body['code']
        if 'status' in response_body:
            self.__status = response_body['status']
        if 'maxRedemptions' in response_body:
            self.__max_redemptions = response_body['maxRedemptions']
        if 'redeemedCount' in response_body:
            self.__redeemed_count = response_body['redeemedCount']
        if 'expiryTime' in response_body:
            self.__expiry_time = response_body['expiryTime']
        if 'createTime' in response_body:
            self.__create_time = response_body['createTime']
