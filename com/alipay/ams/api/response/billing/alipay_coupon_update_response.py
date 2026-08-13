import json
from com.alipay.ams.api.model.result_info import ResultInfo



from com.alipay.ams.api.response.alipay_response import AlipayResponse

class AlipayCouponUpdateResponse(AlipayResponse):
    def __init__(self, rsp_body):
        super(AlipayResponse, self).__init__() 

        self.__result = None  # type: ResultInfo
        self.__coupon_id = None  # type: str
        self.__status = None  # type: str
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
        Updated coupon&#39;s ID. Returned when resultCode is &#x60;SUCCESS&#x60;.
        """
        return self.__coupon_id

    @coupon_id.setter
    def coupon_id(self, value):
        self.__coupon_id = value
    @property
    def status(self):
        """
        Coupon status after update. Returned when resultCode is &#x60;SUCCESS&#x60;.
        """
        return self.__status

    @status.setter
    def status(self, value):
        self.__status = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "result") and self.result is not None:
            params['result'] = self.result
        if hasattr(self, "coupon_id") and self.coupon_id is not None:
            params['couponId'] = self.coupon_id
        if hasattr(self, "status") and self.status is not None:
            params['status'] = self.status
        return params


    def parse_rsp_body(self, response_body):
        response_body = super(AlipayCouponUpdateResponse, self).parse_rsp_body(response_body)
        if 'result' in response_body:
            self.__result = ResultInfo()
            self.__result.parse_rsp_body(response_body['result'])
        if 'couponId' in response_body:
            self.__coupon_id = response_body['couponId']
        if 'status' in response_body:
            self.__status = response_body['status']
