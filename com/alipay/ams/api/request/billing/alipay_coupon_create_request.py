import json
from com.alipay.ams.api.model.amount import Amount
from com.alipay.ams.api.model.coupon_create_applies_to import CouponCreateAppliesTo
from com.alipay.ams.api.model.promotion_code import PromotionCode



from com.alipay.ams.api.request.alipay_request import AlipayRequest

class AlipayCouponCreateRequest(AlipayRequest):
    def __init__(self):
        super(AlipayCouponCreateRequest, self).__init__("/ams/api/v1/billing/coupon/create") 

        self.__coupon_request_id = None  # type: str
        self.__coupon_name = None  # type: str
        self.__discount_type = None  # type: str
        self.__percent_off = None  # type: str
        self.__amount_off = None  # type: Amount
        self.__duration_type = None  # type: str
        self.__duration_value = None  # type: int
        self.__duration_unit = None  # type: str
        self.__max_redemptions = None  # type: int
        self.__redeem_by = None  # type: str
        self.__applies_to = None  # type: CouponCreateAppliesTo
        self.__metadata = None  # type: {str: (str,)}
        self.__promotion_codes = None  # type: [PromotionCode]
        

    @property
    def coupon_request_id(self):
        """
        The coupon request id. Maximum length: 64 characters.
        """
        return self.__coupon_request_id

    @coupon_request_id.setter
    def coupon_request_id(self, value):
        self.__coupon_request_id = value
    @property
    def coupon_name(self):
        """
        The coupon name. Maximum length: 128 characters.
        """
        return self.__coupon_name

    @coupon_name.setter
    def coupon_name(self, value):
        self.__coupon_name = value
    @property
    def discount_type(self):
        """
        The discount type. Maximum length: 16 characters.
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
        """Gets the amount_off of this AlipayCouponCreateRequest.
        
        """
        return self.__amount_off

    @amount_off.setter
    def amount_off(self, value):
        self.__amount_off = value
    @property
    def duration_type(self):
        """
        The duration type. Maximum length: 16 characters.
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
        The max redemptions.
        """
        return self.__max_redemptions

    @max_redemptions.setter
    def max_redemptions(self, value):
        self.__max_redemptions = value
    @property
    def redeem_by(self):
        """
        The redeem by. Maximum length: 24 characters.
        """
        return self.__redeem_by

    @redeem_by.setter
    def redeem_by(self, value):
        self.__redeem_by = value
    @property
    def applies_to(self):
        """Gets the applies_to of this AlipayCouponCreateRequest.
        
        """
        return self.__applies_to

    @applies_to.setter
    def applies_to(self, value):
        self.__applies_to = value
    @property
    def metadata(self):
        """
        Custom metadata for special use cases.
        """
        return self.__metadata

    @metadata.setter
    def metadata(self, value):
        self.__metadata = value
    @property
    def promotion_codes(self):
        """
        The promotion codes.
        """
        return self.__promotion_codes

    @promotion_codes.setter
    def promotion_codes(self, value):
        self.__promotion_codes = value


    def to_ams_json(self): 
        json_str = json.dumps(obj=self.to_ams_dict(), default=lambda o: o.to_ams_dict(), indent=3) 
        return json_str


    def to_ams_dict(self):
        params = dict()
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
        if hasattr(self, "redeem_by") and self.redeem_by is not None:
            params['redeemBy'] = self.redeem_by
        if hasattr(self, "applies_to") and self.applies_to is not None:
            params['appliesTo'] = self.applies_to
        if hasattr(self, "metadata") and self.metadata is not None:
            params['metadata'] = self.metadata
        if hasattr(self, "promotion_codes") and self.promotion_codes is not None:
            params['promotionCodes'] = self.promotion_codes
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
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
        if 'redeemBy' in response_body:
            self.__redeem_by = response_body['redeemBy']
        if 'appliesTo' in response_body:
            self.__applies_to = CouponCreateAppliesTo()
            self.__applies_to.parse_rsp_body(response_body['appliesTo'])
        if 'metadata' in response_body:
            self.__metadata = response_body['metadata']
        if 'promotionCodes' in response_body:
            self.__promotion_codes = []
            for item in response_body['promotionCodes']:
                obj = PromotionCode()
                obj.parse_rsp_body(item)
                self.__promotion_codes.append(obj)
