import json
from com.alipay.ams.api.model.result import Result



from com.alipay.ams.api.response.alipay_response import AlipayResponse

class AlipayPromotionCodeUpdateResponse(AlipayResponse):
    def __init__(self, rsp_body):
        super(AlipayResponse, self).__init__() 

        self.__result = None  # type: Result
        self.__promotion_code_id = None  # type: str
        self.__status = None  # type: str
        self.parse_rsp_body(rsp_body) 


    @property
    def result(self):
        """Gets the result of this AlipayPromotionCodeUpdateResponse.
        
        """
        return self.__result

    @result.setter
    def result(self, value):
        self.__result = value
    @property
    def promotion_code_id(self):
        """
        Updated promotion code&#39;s ID. Returned when resultCode is &#x60;SUCCESS&#x60;.
        """
        return self.__promotion_code_id

    @promotion_code_id.setter
    def promotion_code_id(self, value):
        self.__promotion_code_id = value
    @property
    def status(self):
        """
        Promotion code status after update: &#x60;ACTIVE&#x60; / &#x60;INACTIVE&#x60;. Returned when resultCode is &#x60;SUCCESS&#x60;. Future status values may be added; merchants must handle unrecognized values gracefully (log and skip).
        """
        return self.__status

    @status.setter
    def status(self, value):
        self.__status = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "result") and self.result is not None:
            params['result'] = self.result
        if hasattr(self, "promotion_code_id") and self.promotion_code_id is not None:
            params['promotionCodeId'] = self.promotion_code_id
        if hasattr(self, "status") and self.status is not None:
            params['status'] = self.status
        return params


    def parse_rsp_body(self, response_body):
        response_body = super(AlipayPromotionCodeUpdateResponse, self).parse_rsp_body(response_body)
        if 'result' in response_body:
            self.__result = Result()
            self.__result.parse_rsp_body(response_body['result'])
        if 'promotionCodeId' in response_body:
            self.__promotion_code_id = response_body['promotionCodeId']
        if 'status' in response_body:
            self.__status = response_body['status']
