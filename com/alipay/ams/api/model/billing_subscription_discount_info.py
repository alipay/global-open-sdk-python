import json
from com.alipay.ams.api.model.amount import Amount




class BillingSubscriptionDiscountInfo:
    def __init__(self):
        
        self.__discount_id = None  # type: str
        self.__coupon_id = None  # type: str
        self.__type = None  # type: str
        self.__percent_off = None  # type: int
        self.__amount_off = None  # type: Amount
        self.__duration = None  # type: str
        self.__times = None  # type: int
        self.__status = None  # type: str
        

    @property
    def discount_id(self):
        """
        The discount id. Maximum length: 64 characters.
        """
        return self.__discount_id

    @discount_id.setter
    def discount_id(self, value):
        self.__discount_id = value
    @property
    def coupon_id(self):
        """
        The coupon ID. Maximum length: 64 characters. Note: See documentation for details.
        """
        return self.__coupon_id

    @coupon_id.setter
    def coupon_id(self, value):
        self.__coupon_id = value
    @property
    def type(self):
        """
        The type. Maximum length: 16 characters.
        """
        return self.__type

    @type.setter
    def type(self, value):
        self.__type = value
    @property
    def percent_off(self):
        """
        The percent off. Note: See documentation for details.
        """
        return self.__percent_off

    @percent_off.setter
    def percent_off(self, value):
        self.__percent_off = value
    @property
    def amount_off(self):
        """Gets the amount_off of this BillingSubscriptionDiscountInfo.
        
        """
        return self.__amount_off

    @amount_off.setter
    def amount_off(self, value):
        self.__amount_off = value
    @property
    def duration(self):
        """
        The duration. Maximum length: 16 characters.
        """
        return self.__duration

    @duration.setter
    def duration(self, value):
        self.__duration = value
    @property
    def times(self):
        """
        The times. Note: See documentation for details.
        """
        return self.__times

    @times.setter
    def times(self, value):
        self.__times = value
    @property
    def status(self):
        """
        The current status. Maximum length: 16 characters.
        """
        return self.__status

    @status.setter
    def status(self, value):
        self.__status = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "discount_id") and self.discount_id is not None:
            params['discountId'] = self.discount_id
        if hasattr(self, "coupon_id") and self.coupon_id is not None:
            params['couponId'] = self.coupon_id
        if hasattr(self, "type") and self.type is not None:
            params['type'] = self.type
        if hasattr(self, "percent_off") and self.percent_off is not None:
            params['percentOff'] = self.percent_off
        if hasattr(self, "amount_off") and self.amount_off is not None:
            params['amountOff'] = self.amount_off
        if hasattr(self, "duration") and self.duration is not None:
            params['duration'] = self.duration
        if hasattr(self, "times") and self.times is not None:
            params['times'] = self.times
        if hasattr(self, "status") and self.status is not None:
            params['status'] = self.status
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'discountId' in response_body:
            self.__discount_id = response_body['discountId']
        if 'couponId' in response_body:
            self.__coupon_id = response_body['couponId']
        if 'type' in response_body:
            self.__type = response_body['type']
        if 'percentOff' in response_body:
            self.__percent_off = response_body['percentOff']
        if 'amountOff' in response_body:
            self.__amount_off = Amount()
            self.__amount_off.parse_rsp_body(response_body['amountOff'])
        if 'duration' in response_body:
            self.__duration = response_body['duration']
        if 'times' in response_body:
            self.__times = response_body['times']
        if 'status' in response_body:
            self.__status = response_body['status']
