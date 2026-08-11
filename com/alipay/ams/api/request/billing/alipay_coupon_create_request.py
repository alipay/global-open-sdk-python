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
        self.__redeem_by = None  # type: str
        self.__applies_to = None  # type: CouponCreateAppliesTo
        self.__metadata = None  # type: str
        self.__promotion_codes = None  # type: [PromotionCode]
        self.__max_redemptions = None  # type: int
        

    @property
    def coupon_request_id(self):
        """
        Merchant-supplied idempotency key for this create request. Must be unique per merchant. Cannot be empty. Maximum length: 64 characters. Idempotent replay: if a request is repeated with the same &#x60;couponRequestId&#x60; and the same parameters, the API returns &#x60;SUCCESS&#x60; together with the previously created coupon (no new coupon is created); a replay with different parameters returns &#x60;PARAM_ILLEGAL&#x60;.
        """
        return self.__coupon_request_id

    @coupon_request_id.setter
    def coupon_request_id(self, value):
        self.__coupon_request_id = value
    @property
    def coupon_name(self):
        """
        Display name for the coupon. Maximum length: 128 characters.
        """
        return self.__coupon_name

    @coupon_name.setter
    def coupon_name(self, value):
        self.__coupon_name = value
    @property
    def discount_type(self):
        """
        Type of discount. Allowed values: &#x60;PERCENT&#x60; (percentage off) or &#x60;AMOUNT&#x60; (fixed amount off). Cannot be empty.
        """
        return self.__discount_type

    @discount_type.setter
    def discount_type(self, value):
        self.__discount_type = value
    @property
    def percent_off(self):
        """
        Percentage discount value. Up to 2 decimal places. Value range: 0.01-100.00. Examples: &#x60;20&#x60; (20% off), &#x60;33.33&#x60; (33.33% off), &#x60;100&#x60; (100% off / free). Values with more than 2 decimal places (e.g. &#x60;33.333&#x60;) are rejected with &#x60;PARAM_ILLEGAL&#x60;. Required when &#x60;discountType&#x60; &#x3D; &#x60;PERCENT&#x60;; must be null when &#x60;discountType&#x60; &#x3D; &#x60;AMOUNT&#x60;.
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
        How long the discount applies to a subscription. Allowed values: &#x60;ONCE&#x60; (applied once on the next invoice only; discount is marked EXPIRED immediately after the first invoice), &#x60;REPEATING&#x60; (applied for a calendar duration defined by &#x60;durationValue&#x60; x &#x60;durationUnit&#x60; - see below for detailed semantics), &#x60;FOREVER&#x60; (applied indefinitely to all future invoices; discount remains ACTIVE until manually deactivated).
        """
        return self.__duration_type

    @duration_type.setter
    def duration_type(self, value):
        self.__duration_type = value
    @property
    def duration_value(self):
        """
        The numeric component of the coupon&#39;s calendar duration. Required when &#x60;durationType&#x60; &#x3D; &#x60;REPEATING&#x60;; must be null otherwise. Combined with &#x60;durationUnit&#x60;, it defines a half-open time window &#x60;[startTime, startTime + durationValue x durationUnit)&#x60; starting from the coupon&#39;s first application to a subscription. At each billing cycle, the system uses the billing period start time (not the invoice generation task&#39;s execution time) as the reference point to check the window. If the reference time is before the expiry boundary, the full discount is applied to the invoice; if the reference time is at or after the boundary, the discount is not applied and is marked EXPIRED. No proration is performed for partial overlap. Value range: 1-120. Examples: (1) &#x60;durationValue&#x3D;3, durationUnit&#x3D;MONTH&#x60; -&gt; coupon effective for 3 calendar months from first use; a monthly subscription receives the discount on 3 invoices. (2) &#x60;durationValue&#x3D;2, durationUnit&#x3D;WEEK&#x60; -&gt; effective for 2 calendar weeks (14 days); a monthly subscription only receives the discount on the first invoice. (3) &#x60;durationValue&#x3D;21, durationUnit&#x3D;DAY&#x60; -&gt; effective for 21 calendar days; a monthly subscription only receives the discount on the first invoice (billing period start of the second invoice is ~30 days later, outside the window).
        """
        return self.__duration_value

    @duration_value.setter
    def duration_value(self, value):
        self.__duration_value = value
    @property
    def duration_unit(self):
        """
        The time unit for the coupon duration. Required when &#x60;durationType&#x60; is &#x60;REPEATING&#x60;. Allowed values are &#x60;DAY&#x60;, &#x60;WEEK&#x60;, &#x60;MONTH&#x60;, and &#x60;YEAR&#x60;. Combined with &#x60;durationValue&#x60; to define the calendar-based effective window.
        """
        return self.__duration_unit

    @duration_unit.setter
    def duration_unit(self, value):
        self.__duration_unit = value
    @property
    def redeem_by(self):
        """
        UTC timestamp (ISO 8601) after which the coupon can no longer be redeemed. If not set, the coupon has no expiry.
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
        Merchant-defined key-value pairs stored as JSON string. Enforced constraints: max 50 keys; each key max 40 characters; each value max 500 characters. Requests exceeding these limits return &#x60;PARAM_ILLEGAL&#x60;. The value must be a valid JSON object string.
        """
        return self.__metadata

    @metadata.setter
    def metadata(self, value):
        self.__metadata = value
    @property
    def promotion_codes(self):
        """
        Optional nested promotion code descriptors. When non-empty, the server atomically creates the coupon and all listed promotion codes in a single transaction. When provided, each element must include &#x60;promotionCodeRequestId&#x60;. Maximum size: 10. See Section 4.2.3.7 for PromotionCodeCreateInfo structure.
        """
        return self.__promotion_codes

    @promotion_codes.setter
    def promotion_codes(self, value):
        self.__promotion_codes = value
    @property
    def max_redemptions(self):
        """
        Maximum number of times the coupon can be redeemed across all promotion codes. If not set or set to 0, redemptions are unlimited. Value range: 0-999999.
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
        if hasattr(self, "redeem_by") and self.redeem_by is not None:
            params['redeemBy'] = self.redeem_by
        if hasattr(self, "applies_to") and self.applies_to is not None:
            params['appliesTo'] = self.applies_to
        if hasattr(self, "metadata") and self.metadata is not None:
            params['metadata'] = self.metadata
        if hasattr(self, "promotion_codes") and self.promotion_codes is not None:
            params['promotionCodes'] = self.promotion_codes
        if hasattr(self, "max_redemptions") and self.max_redemptions is not None:
            params['maxRedemptions'] = self.max_redemptions
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
        if 'maxRedemptions' in response_body:
            self.__max_redemptions = response_body['maxRedemptions']
