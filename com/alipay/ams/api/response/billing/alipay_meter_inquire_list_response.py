import json
from com.alipay.ams.api.model.result import Result
from com.alipay.ams.api.model.meter import Meter



from com.alipay.ams.api.response.alipay_response import AlipayResponse

class AlipayMeterInquireListResponse(AlipayResponse):
    def __init__(self, rsp_body):
        super(AlipayResponse, self).__init__() 

        self.__result = None  # type: Result
        self.__meters = None  # type: [Meter]
        self.parse_rsp_body(rsp_body) 


    @property
    def result(self):
        """Gets the result of this AlipayMeterInquireListResponse.
        
        """
        return self.__result

    @result.setter
    def result(self, value):
        self.__result = value
    @property
    def meters(self):
        """
        The meters. Note: See documentation for details.
        """
        return self.__meters

    @meters.setter
    def meters(self, value):
        self.__meters = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "result") and self.result is not None:
            params['result'] = self.result
        if hasattr(self, "meters") and self.meters is not None:
            params['meters'] = self.meters
        return params


    def parse_rsp_body(self, response_body):
        response_body = super(AlipayMeterInquireListResponse, self).parse_rsp_body(response_body)
        if 'result' in response_body:
            self.__result = Result()
            self.__result.parse_rsp_body(response_body['result'])
        if 'meters' in response_body:
            self.__meters = []
            for item in response_body['meters']:
                obj = Meter()
                obj.parse_rsp_body(item)
                self.__meters.append(obj)
