import json
from com.alipay.ams.api.model.amount import Amount




class Coupon:
    def __init__(self):
        
        self.__coupon_id = None  # type: str
        self.__coupon_name = None  # type: str
        self.__discount_type = None  # type: str
        self.__percent_off = None  # type: str
        self.__amount_off = None  # type: Amount
        self.__redeem_by = None  # type: str
        self.__status = None  # type: str
        self.__max_redemptions = None  # type: int
        self.__redeemed_count = None  # type: int
        

    @property
    def coupon_id(self):
        """
        System-generated coupon ID.
        """
        return self.__coupon_id

    @coupon_id.setter
    def coupon_id(self, value):
        self.__coupon_id = value
    @property
    def coupon_name(self):
        """
        Coupon display name.
        """
        return self.__coupon_name

    @coupon_name.setter
    def coupon_name(self, value):
        self.__coupon_name = value
    @property
    def discount_type(self):
        """
        Filter by discount type. Allowed values: &#x60;PERCENT&#x60;, &#x60;AMOUNT&#x60;. If not provided, returns all discount types.
        """
        return self.__discount_type

    @discount_type.setter
    def discount_type(self, value):
        self.__discount_type = value
    @property
    def percent_off(self):
        """
        Percentage discount (up to 2 decimal places). Returned when &#x60;discountType&#x60; &#x3D; &#x60;PERCENT&#x60;.
        """
        return self.__percent_off

    @percent_off.setter
    def percent_off(self, value):
        self.__percent_off = value
    @property
    def amount_off(self):
        """Gets the amount_off of this Coupon.
        
        """
        return self.__amount_off

    @amount_off.setter
    def amount_off(self, value):
        self.__amount_off = value
    @property
    def redeem_by(self):
        """
        Redemption expiry time.
        """
        return self.__redeem_by

    @redeem_by.setter
    def redeem_by(self, value):
        self.__redeem_by = value
    @property
    def status(self):
        """
        Filter by coupon status. Allowed values: &#x60;ACTIVE&#x60;, &#x60;INACTIVE&#x60;. If not provided, returns coupons of all statuses.
        """
        return self.__status

    @status.setter
    def status(self, value):
        self.__status = value
    @property
    def max_redemptions(self):
        """
        The maximum redemption count.
        """
        return self.__max_redemptions

    @max_redemptions.setter
    def max_redemptions(self, value):
        self.__max_redemptions = value
    @property
    def redeemed_count(self):
        """
        The number of times the coupon has been redeemed.
        """
        return self.__redeemed_count

    @redeemed_count.setter
    def redeemed_count(self, value):
        self.__redeemed_count = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "coupon_id") and self.coupon_id is not None:
            params['couponId'] = self.coupon_id
        if hasattr(self, "coupon_name") and self.coupon_name is not None:
            params['couponName'] = self.coupon_name
        if hasattr(self, "discount_type") and self.discount_type is not None:
            params['discountType'] = self.discount_type
        if hasattr(self, "percent_off") and self.percent_off is not None:
            params['percentOff'] = self.percent_off
        if hasattr(self, "amount_off") and self.amount_off is not None:
            params['amountOff'] = self.amount_off
        if hasattr(self, "redeem_by") and self.redeem_by is not None:
            params['redeemBy'] = self.redeem_by
        if hasattr(self, "status") and self.status is not None:
            params['status'] = self.status
        if hasattr(self, "max_redemptions") and self.max_redemptions is not None:
            params['maxRedemptions'] = self.max_redemptions
        if hasattr(self, "redeemed_count") and self.redeemed_count is not None:
            params['redeemedCount'] = self.redeemed_count
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'couponId' in response_body:
            self.__coupon_id = response_body['couponId']
        if 'couponName' in response_body:
            self.__coupon_name = response_body['couponName']
        if 'discountType' in response_body:
            self.__discount_type = response_body['discountType']
        if 'percentOff' in response_body:
            self.__percent_off = response_body['percentOff']
        if 'amountOff' in response_body:
            self.__amount_off = Amount()
            self.__amount_off.parse_rsp_body(response_body['amountOff'])
        if 'redeemBy' in response_body:
            self.__redeem_by = response_body['redeemBy']
        if 'status' in response_body:
            self.__status = response_body['status']
        if 'maxRedemptions' in response_body:
            self.__max_redemptions = response_body['maxRedemptions']
        if 'redeemedCount' in response_body:
            self.__redeemed_count = response_body['redeemedCount']
