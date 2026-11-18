import json
from com.alipay.ams.api.model.result import Result
from com.alipay.ams.api.model.reserve_hold_detail import ReserveHoldDetail



from com.alipay.ams.api.response.alipay_response import AlipayResponse

class AlipayInquireHoldListResponse(AlipayResponse):
    def __init__(self, rsp_body):
        super(AlipayResponse, self).__init__() 

        self.__result = None  # type: Result
        self.__hold_details = None  # type: [ReserveHoldDetail]
        self.__has_more = None  # type: bool
        self.parse_rsp_body(rsp_body) 


    @property
    def result(self):
        """Gets the result of this AlipayInquireHoldListResponse.
        
        """
        return self.__result

    @result.setter
    def result(self, value):
        self.__result = value
    @property
    def hold_details(self):
        """
        The manual holds returned in descending holdId order. At most limit items are returned, and limit cannot exceed 100. Returned when result.resultStatus is S.
        """
        return self.__hold_details

    @hold_details.setter
    def hold_details(self, value):
        self.__hold_details = value
    @property
    def has_more(self):
        """
        Whether more records exist in the direction requested by the current cursor. Exact-query mode always returns false. Returned when result.resultStatus is S.
        """
        return self.__has_more

    @has_more.setter
    def has_more(self, value):
        self.__has_more = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "result") and self.result is not None:
            params['result'] = self.result
        if hasattr(self, "hold_details") and self.hold_details is not None:
            params['holdDetails'] = self.hold_details
        if hasattr(self, "has_more") and self.has_more is not None:
            params['hasMore'] = self.has_more
        return params


    def parse_rsp_body(self, response_body):
        response_body = super(AlipayInquireHoldListResponse, self).parse_rsp_body(response_body)
        if 'result' in response_body:
            self.__result = Result()
            self.__result.parse_rsp_body(response_body['result'])
        if 'holdDetails' in response_body:
            self.__hold_details = []
            for item in response_body['holdDetails']:
                obj = ReserveHoldDetail()
                obj.parse_rsp_body(item)
                self.__hold_details.append(obj)
        if 'hasMore' in response_body:
            self.__has_more = response_body['hasMore']
