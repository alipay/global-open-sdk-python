import json
from com.alipay.ams.api.model.coupon_create_result import CouponCreateResult
from com.alipay.ams.api.model.promotion_code import PromotionCode



from com.alipay.ams.api.response.alipay_response import AlipayResponse

class AlipayCouponCreateResponse(AlipayResponse):
    def __init__(self, rsp_body):
        super(AlipayResponse, self).__init__() 

        self.__result = None  # type: CouponCreateResult
        self.__coupon_id = None  # type: str
        self.__coupon_name = None  # type: str
        self.__discount_type = None  # type: str
        self.__status = None  # type: str
        self.__promotion_codes = None  # type: [PromotionCode]
        self.parse_rsp_body(rsp_body) 


    @property
    def result(self):
        """Gets the result of this AlipayCouponCreateResponse.
        
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
    def discount_type(self):
        """
        The discount type. Maximum length: 16 characters. Note: See documentation for details.
        """
        return self.__discount_type

    @discount_type.setter
    def discount_type(self, value):
        self.__discount_type = value
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
    def promotion_codes(self):
        """
        The promotion codes. Note: See documentation for details.
        """
        return self.__promotion_codes

    @promotion_codes.setter
    def promotion_codes(self, value):
        self.__promotion_codes = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "result") and self.result is not None:
            params['result'] = self.result
        if hasattr(self, "coupon_id") and self.coupon_id is not None:
            params['couponId'] = self.coupon_id
        if hasattr(self, "coupon_name") and self.coupon_name is not None:
            params['couponName'] = self.coupon_name
        if hasattr(self, "discount_type") and self.discount_type is not None:
            params['discountType'] = self.discount_type
        if hasattr(self, "status") and self.status is not None:
            params['status'] = self.status
        if hasattr(self, "promotion_codes") and self.promotion_codes is not None:
            params['promotionCodes'] = self.promotion_codes
        return params


    def parse_rsp_body(self, response_body):
        response_body = super(AlipayCouponCreateResponse, self).parse_rsp_body(response_body)
        if 'result' in response_body:
            self.__result = CouponCreateResult()
            self.__result.parse_rsp_body(response_body['result'])
        if 'couponId' in response_body:
            self.__coupon_id = response_body['couponId']
        if 'couponName' in response_body:
            self.__coupon_name = response_body['couponName']
        if 'discountType' in response_body:
            self.__discount_type = response_body['discountType']
        if 'status' in response_body:
            self.__status = response_body['status']
        if 'promotionCodes' in response_body:
            self.__promotion_codes = []
            for item in response_body['promotionCodes']:
                obj = PromotionCode()
                obj.parse_rsp_body(item)
                self.__promotion_codes.append(obj)
