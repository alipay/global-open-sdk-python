import json
from com.alipay.ams.api.model.result_info import ResultInfo
from com.alipay.ams.api.model.amount import Amount
from com.alipay.ams.api.model.coupon_inquire_details_applies_to import CouponInquireDetailsAppliesTo



from com.alipay.ams.api.response.alipay_response import AlipayResponse

class AlipayCouponInquireDetailsResponse(AlipayResponse):
    def __init__(self, rsp_body):
        super(AlipayResponse, self).__init__() 

        self.__result = None  # type: ResultInfo
        self.__coupon_id = None  # type: str
        self.__coupon_request_id = None  # type: str
        self.__coupon_name = None  # type: str
        self.__discount_type = None  # type: str
        self.__percent_off = None  # type: str
        self.__amount_off = None  # type: Amount
        self.__duration_type = None  # type: str
        self.__duration_value = None  # type: int
        self.__duration_unit = None  # type: str
        self.__max_redemptions = None  # type: int
        self.__redeemed_count = None  # type: int
        self.__redeem_by = None  # type: str
        self.__applies_to = None  # type: CouponInquireDetailsAppliesTo
        self.__status = None  # type: str
        self.__metadata = None  # type: {str: (str,)}
        self.__create_time = None  # type: str
        self.parse_rsp_body(rsp_body) 


    @property
    def result(self):
        """Gets the result of this AlipayCouponInquireDetailsResponse.
        
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
    def coupon_request_id(self):
        """
        The coupon request id. Maximum length: 64 characters. Note: See documentation for details.
        """
        return self.__coupon_request_id

    @coupon_request_id.setter
    def coupon_request_id(self, value):
        self.__coupon_request_id = value
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
    def discount_type(self):
        """
        The discount type. Maximum length: 16 characters. Note: See documentation for details.
        """
        return self.__discount_type

    @discount_type.setter
    def discount_type(self, value):
        self.__discount_type = value
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
        """Gets the amount_off of this AlipayCouponInquireDetailsResponse.
        
        """
        return self.__amount_off

    @amount_off.setter
    def amount_off(self, value):
        self.__amount_off = value
    @property
    def duration_type(self):
        """
        The duration type. Maximum length: 16 characters. Note: See documentation for details.
        """
        return self.__duration_type

    @duration_type.setter
    def duration_type(self, value):
        self.__duration_type = value
    @property
    def duration_value(self):
        """
        The duration value. Note: See documentation for details.
        """
        return self.__duration_value

    @duration_value.setter
    def duration_value(self, value):
        self.__duration_value = value
    @property
    def duration_unit(self):
        """
        The duration unit. Maximum length: 16 characters. Note: See documentation for details.
        """
        return self.__duration_unit

    @duration_unit.setter
    def duration_unit(self, value):
        self.__duration_unit = value
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
    def applies_to(self):
        """Gets the applies_to of this AlipayCouponInquireDetailsResponse.
        
        """
        return self.__applies_to

    @applies_to.setter
    def applies_to(self, value):
        self.__applies_to = value
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
    def metadata(self):
        """
        Custom metadata for special use cases. Maximum length: 65535 characters. Note: See documentation for details.
        """
        return self.__metadata

    @metadata.setter
    def metadata(self, value):
        self.__metadata = value
    @property
    def create_time(self):
        """
        The create time. Note: See documentation for details.
        """
        return self.__create_time

    @create_time.setter
    def create_time(self, value):
        self.__create_time = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "result") and self.result is not None:
            params['result'] = self.result
        if hasattr(self, "coupon_id") and self.coupon_id is not None:
            params['couponId'] = self.coupon_id
        if hasattr(self, "coupon_request_id") and self.coupon_request_id is not None:
            params['couponRequestId'] = self.coupon_request_id
        if hasattr(self, "coupon_name") and self.coupon_name is not None:
            params['couponName'] = self.coupon_name
        if hasattr(self, "discount_type") and self.discount_type is not None:
            params['discountType'] = self.discount_type
        if hasattr(self, "percent_off") and self.percent_off is not None:
            params['percentOff'] = self.percent_off
        if hasattr(self, "amount_off") and self.amount_off is not None:
            params['amountOff'] = self.amount_off
        if hasattr(self, "duration_type") and self.duration_type is not None:
            params['durationType'] = self.duration_type
        if hasattr(self, "duration_value") and self.duration_value is not None:
            params['durationValue'] = self.duration_value
        if hasattr(self, "duration_unit") and self.duration_unit is not None:
            params['durationUnit'] = self.duration_unit
        if hasattr(self, "max_redemptions") and self.max_redemptions is not None:
            params['maxRedemptions'] = self.max_redemptions
        if hasattr(self, "redeemed_count") and self.redeemed_count is not None:
            params['redeemedCount'] = self.redeemed_count
        if hasattr(self, "redeem_by") and self.redeem_by is not None:
            params['redeemBy'] = self.redeem_by
        if hasattr(self, "applies_to") and self.applies_to is not None:
            params['appliesTo'] = self.applies_to
        if hasattr(self, "status") and self.status is not None:
            params['status'] = self.status
        if hasattr(self, "metadata") and self.metadata is not None:
            params['metadata'] = self.metadata
        if hasattr(self, "create_time") and self.create_time is not None:
            params['createTime'] = self.create_time
        return params


    def parse_rsp_body(self, response_body):
        response_body = super(AlipayCouponInquireDetailsResponse, self).parse_rsp_body(response_body)
        if 'result' in response_body:
            self.__result = ResultInfo()
            self.__result.parse_rsp_body(response_body['result'])
        if 'couponId' in response_body:
            self.__coupon_id = response_body['couponId']
        if 'couponRequestId' in response_body:
            self.__coupon_request_id = response_body['couponRequestId']
        if 'couponName' in response_body:
            self.__coupon_name = response_body['couponName']
        if 'discountType' in response_body:
            self.__discount_type = response_body['discountType']
        if 'percentOff' in response_body:
            self.__percent_off = response_body['percentOff']
        if 'amountOff' in response_body:
            self.__amount_off = Amount()
            self.__amount_off.parse_rsp_body(response_body['amountOff'])
        if 'durationType' in response_body:
            self.__duration_type = response_body['durationType']
        if 'durationValue' in response_body:
            self.__duration_value = response_body['durationValue']
        if 'durationUnit' in response_body:
            self.__duration_unit = response_body['durationUnit']
        if 'maxRedemptions' in response_body:
            self.__max_redemptions = response_body['maxRedemptions']
        if 'redeemedCount' in response_body:
            self.__redeemed_count = response_body['redeemedCount']
        if 'redeemBy' in response_body:
            self.__redeem_by = response_body['redeemBy']
        if 'appliesTo' in response_body:
            self.__applies_to = CouponInquireDetailsAppliesTo()
            self.__applies_to.parse_rsp_body(response_body['appliesTo'])
        if 'status' in response_body:
            self.__status = response_body['status']
        if 'metadata' in response_body:
            self.__metadata = response_body['metadata']
        if 'createTime' in response_body:
            self.__create_time = response_body['createTime']
