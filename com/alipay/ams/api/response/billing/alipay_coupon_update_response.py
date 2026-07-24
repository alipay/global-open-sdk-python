import json
from com.alipay.ams.api.model.coupon_update_result import CouponUpdateResult



from com.alipay.ams.api.response.alipay_response import AlipayResponse

class AlipayCouponUpdateResponse(AlipayResponse):
    def __init__(self, rsp_body):
        super(AlipayResponse, self).__init__() 

        self.__result = None  # type: CouponUpdateResult
        self.__coupon_id = None  # type: str
        self.__coupon_name = None  # type: str
        self.__status = None  # type: str
        self.__max_redemptions = None  # type: int
        self.__redeemed_count = None  # type: int
        self.__redeem_by = None  # type: str
        self.__metadata = None  # type: {str: (str,)}
        self.__update_time = None  # type: str
        self.parse_rsp_body(rsp_body) 


    @property
    def result(self):
        """Gets the result of this AlipayCouponUpdateResponse.
        
        """
        return self.__result

    @result.setter
    def result(self, value):
        self.__result = value
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
    def coupon_name(self):
        """
        The coupon name. Maximum length: 128 characters. Note: See documentation for details.
        """
        return self.__coupon_name

    @coupon_name.setter
    def coupon_name(self, value):
        self.__coupon_name = value
    @property
    def status(self):
        """
        The current status. Maximum length: 16 characters. Note: See documentation for details.
        """
        return self.__status

    @status.setter
    def status(self, value):
        self.__status = value
    @property
    def max_redemptions(self):
        """
        The max redemptions. Note: See documentation for details.
        """
        return self.__max_redemptions

    @max_redemptions.setter
    def max_redemptions(self, value):
        self.__max_redemptions = value
    @property
    def redeemed_count(self):
        """
        The redeemed count. Note: See documentation for details.
        """
        return self.__redeemed_count

    @redeemed_count.setter
    def redeemed_count(self, value):
        self.__redeemed_count = value
    @property
    def redeem_by(self):
        """
        The redeem by. Note: See documentation for details.
        """
        return self.__redeem_by

    @redeem_by.setter
    def redeem_by(self, value):
        self.__redeem_by = value
    @property
    def metadata(self):
        """
        Custom metadata for special use cases. Maximum length: 65535 characters. Note: See documentation for details.
        """
        return self.__metadata

    @metadata.setter
    def metadata(self, value):
        self.__metadata = value
    @property
    def update_time(self):
        """
        The update time. Note: See documentation for details.
        """
        return self.__update_time

    @update_time.setter
    def update_time(self, value):
        self.__update_time = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "result") and self.result is not None:
            params['result'] = self.result
        if hasattr(self, "coupon_id") and self.coupon_id is not None:
            params['couponId'] = self.coupon_id
        if hasattr(self, "coupon_name") and self.coupon_name is not None:
            params['couponName'] = self.coupon_name
        if hasattr(self, "status") and self.status is not None:
            params['status'] = self.status
        if hasattr(self, "max_redemptions") and self.max_redemptions is not None:
            params['maxRedemptions'] = self.max_redemptions
        if hasattr(self, "redeemed_count") and self.redeemed_count is not None:
            params['redeemedCount'] = self.redeemed_count
        if hasattr(self, "redeem_by") and self.redeem_by is not None:
            params['redeemBy'] = self.redeem_by
        if hasattr(self, "metadata") and self.metadata is not None:
            params['metadata'] = self.metadata
        if hasattr(self, "update_time") and self.update_time is not None:
            params['updateTime'] = self.update_time
        return params


    def parse_rsp_body(self, response_body):
        response_body = super(AlipayCouponUpdateResponse, self).parse_rsp_body(response_body)
        if 'result' in response_body:
            self.__result = CouponUpdateResult()
            self.__result.parse_rsp_body(response_body['result'])
        if 'couponId' in response_body:
            self.__coupon_id = response_body['couponId']
        if 'couponName' in response_body:
            self.__coupon_name = response_body['couponName']
        if 'status' in response_body:
            self.__status = response_body['status']
        if 'maxRedemptions' in response_body:
            self.__max_redemptions = response_body['maxRedemptions']
        if 'redeemedCount' in response_body:
            self.__redeemed_count = response_body['redeemedCount']
        if 'redeemBy' in response_body:
            self.__redeem_by = response_body['redeemBy']
        if 'metadata' in response_body:
            self.__metadata = response_body['metadata']
        if 'updateTime' in response_body:
            self.__update_time = response_body['updateTime']
