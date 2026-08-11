import json
from com.alipay.ams.api.model.result import Result
from com.alipay.ams.api.model.promotion_code_inquire_details_min_amount import PromotionCodeInquireDetailsMinAmount



from com.alipay.ams.api.response.alipay_response import AlipayResponse

class AlipayPromotionCodeInquireDetailsResponse(AlipayResponse):
    def __init__(self, rsp_body):
        super(AlipayResponse, self).__init__() 

        self.__result = None  # type: Result
        self.__promotion_code_id = None  # type: str
        self.__promotion_code_request_id = None  # type: str
        self.__code = None  # type: str
        self.__coupon_id = None  # type: str
        self.__status = None  # type: str
        self.__max_redemptions = None  # type: int
        self.__redeemed_count = None  # type: int
        self.__expiry_time = None  # type: str
        self.__min_amount = None  # type: PromotionCodeInquireDetailsMinAmount
        self.__one_time_only = None  # type: bool
        self.__customer_id = None  # type: str
        self.__metadata = None  # type: str
        self.__create_time = None  # type: str
        self.parse_rsp_body(rsp_body) 


    @property
    def result(self):
        """Gets the result of this AlipayPromotionCodeInquireDetailsResponse.
        
        """
        return self.__result

    @result.setter
    def result(self, value):
        self.__result = value
    @property
    def promotion_code_id(self):
        """
        System-generated promotion code ID. Returned when resultCode is &#x60;SUCCESS&#x60;.
        """
        return self.__promotion_code_id

    @promotion_code_id.setter
    def promotion_code_id(self, value):
        self.__promotion_code_id = value
    @property
    def promotion_code_request_id(self):
        """
        Merchant-supplied idempotency key used at creation. Returned when resultCode is &#x60;SUCCESS&#x60;.
        """
        return self.__promotion_code_request_id

    @promotion_code_request_id.setter
    def promotion_code_request_id(self, value):
        self.__promotion_code_request_id = value
    @property
    def code(self):
        """
        The promotion code string. Returned when resultCode is &#x60;SUCCESS&#x60;.
        """
        return self.__code

    @code.setter
    def code(self, value):
        self.__code = value
    @property
    def coupon_id(self):
        """
        Parent coupon&#39;s ID. Returned when resultCode is &#x60;SUCCESS&#x60;.
        """
        return self.__coupon_id

    @coupon_id.setter
    def coupon_id(self, value):
        self.__coupon_id = value
    @property
    def status(self):
        """
        Promotion code status: &#x60;ACTIVE&#x60; / &#x60;INACTIVE&#x60; only - the DB persists these two values and no &#x60;EXPIRED&#x60; status is derived at read time. A promotion code past its &#x60;expiryTime&#x60; is no longer redeemable; compare &#x60;expiryTime&#x60; to the current time to detect expiry. Future status values may be added; merchants must handle unrecognized values gracefully (log and skip). Returned only when result.resultCode is SUCCESS.
        """
        return self.__status

    @status.setter
    def status(self, value):
        self.__status = value
    @property
    def max_redemptions(self):
        """
        Maximum redemption count. Value range: 0-999999. Returned when resultCode is &#x60;SUCCESS&#x60;.
        """
        return self.__max_redemptions

    @max_redemptions.setter
    def max_redemptions(self, value):
        self.__max_redemptions = value
    @property
    def redeemed_count(self):
        """
        Number of times the promotion code has been redeemed. Value range: 0-999999. Returned when resultCode is &#x60;SUCCESS&#x60;.
        """
        return self.__redeemed_count

    @redeemed_count.setter
    def redeemed_count(self, value):
        self.__redeemed_count = value
    @property
    def expiry_time(self):
        """
        Expiry time (UTC, ISO 8601). Returned when resultCode is &#x60;SUCCESS&#x60; and the field was set.
        """
        return self.__expiry_time

    @expiry_time.setter
    def expiry_time(self, value):
        self.__expiry_time = value
    @property
    def min_amount(self):
        """Gets the min_amount of this AlipayPromotionCodeInquireDetailsResponse.
        
        """
        return self.__min_amount

    @min_amount.setter
    def min_amount(self, value):
        self.__min_amount = value
    @property
    def one_time_only(self):
        """
        Whether code is one-time per customer. Returned when resultCode is &#x60;SUCCESS&#x60;.
        """
        return self.__one_time_only

    @one_time_only.setter
    def one_time_only(self, value):
        self.__one_time_only = value
    @property
    def customer_id(self):
        """
        Restricted customer&#39;s ID. Returned when resultCode is &#x60;SUCCESS&#x60; and the field was set.
        """
        return self.__customer_id

    @customer_id.setter
    def customer_id(self, value):
        self.__customer_id = value
    @property
    def metadata(self):
        """
        Merchant-defined key-value pairs. Returned when resultCode is &#x60;SUCCESS&#x60; and the field was set. The value must be a valid JSON object string.
        """
        return self.__metadata

    @metadata.setter
    def metadata(self, value):
        self.__metadata = value
    @property
    def create_time(self):
        """
        Creation time (UTC, ISO 8601). Returned when resultCode is &#x60;SUCCESS&#x60;.
        """
        return self.__create_time

    @create_time.setter
    def create_time(self, value):
        self.__create_time = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "result") and self.result is not None:
            params['result'] = self.result
        if hasattr(self, "promotion_code_id") and self.promotion_code_id is not None:
            params['promotionCodeId'] = self.promotion_code_id
        if hasattr(self, "promotion_code_request_id") and self.promotion_code_request_id is not None:
            params['promotionCodeRequestId'] = self.promotion_code_request_id
        if hasattr(self, "code") and self.code is not None:
            params['code'] = self.code
        if hasattr(self, "coupon_id") and self.coupon_id is not None:
            params['couponId'] = self.coupon_id
        if hasattr(self, "status") and self.status is not None:
            params['status'] = self.status
        if hasattr(self, "max_redemptions") and self.max_redemptions is not None:
            params['maxRedemptions'] = self.max_redemptions
        if hasattr(self, "redeemed_count") and self.redeemed_count is not None:
            params['redeemedCount'] = self.redeemed_count
        if hasattr(self, "expiry_time") and self.expiry_time is not None:
            params['expiryTime'] = self.expiry_time
        if hasattr(self, "min_amount") and self.min_amount is not None:
            params['minAmount'] = self.min_amount
        if hasattr(self, "one_time_only") and self.one_time_only is not None:
            params['oneTimeOnly'] = self.one_time_only
        if hasattr(self, "customer_id") and self.customer_id is not None:
            params['customerId'] = self.customer_id
        if hasattr(self, "metadata") and self.metadata is not None:
            params['metadata'] = self.metadata
        if hasattr(self, "create_time") and self.create_time is not None:
            params['createTime'] = self.create_time
        return params


    def parse_rsp_body(self, response_body):
        response_body = super(AlipayPromotionCodeInquireDetailsResponse, self).parse_rsp_body(response_body)
        if 'result' in response_body:
            self.__result = Result()
            self.__result.parse_rsp_body(response_body['result'])
        if 'promotionCodeId' in response_body:
            self.__promotion_code_id = response_body['promotionCodeId']
        if 'promotionCodeRequestId' in response_body:
            self.__promotion_code_request_id = response_body['promotionCodeRequestId']
        if 'code' in response_body:
            self.__code = response_body['code']
        if 'couponId' in response_body:
            self.__coupon_id = response_body['couponId']
        if 'status' in response_body:
            self.__status = response_body['status']
        if 'maxRedemptions' in response_body:
            self.__max_redemptions = response_body['maxRedemptions']
        if 'redeemedCount' in response_body:
            self.__redeemed_count = response_body['redeemedCount']
        if 'expiryTime' in response_body:
            self.__expiry_time = response_body['expiryTime']
        if 'minAmount' in response_body:
            self.__min_amount = PromotionCodeInquireDetailsMinAmount()
            self.__min_amount.parse_rsp_body(response_body['minAmount'])
        if 'oneTimeOnly' in response_body:
            self.__one_time_only = response_body['oneTimeOnly']
        if 'customerId' in response_body:
            self.__customer_id = response_body['customerId']
        if 'metadata' in response_body:
            self.__metadata = response_body['metadata']
        if 'createTime' in response_body:
            self.__create_time = response_body['createTime']
