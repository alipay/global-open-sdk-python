import json
from com.alipay.ams.api.model.rate_result import RateResult
from com.alipay.ams.api.model.result import Result



from com.alipay.ams.api.response.alipay_response import AlipayResponse

class AlipayInquiryRateResponse(AlipayResponse):
    def __init__(self, rsp_body):
        super(AlipayResponse, self).__init__() 

        self.__rate_result_list = None  # type: [RateResult]
        self.__result = None  # type: Result
        self.parse_rsp_body(rsp_body) 


    @property
    def rate_result_list(self):
        """Gets the rate_result_list of this AlipayInquiryRateResponse.
        
        """
        return self.__rate_result_list

    @rate_result_list.setter
    def rate_result_list(self, value):
        self.__rate_result_list = value
    @property
    def result(self):
        """Gets the result of this AlipayInquiryRateResponse.
        
        """
        return self.__result

    @result.setter
    def result(self, value):
        self.__result = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "rate_result_list") and self.rate_result_list is not None:
            params['rateResultList'] = self.rate_result_list
        if hasattr(self, "result") and self.result is not None:
            params['result'] = self.result
        return params


    def parse_rsp_body(self, response_body):
        response_body = super(AlipayInquiryRateResponse, self).parse_rsp_body(response_body)
        if 'rateResultList' in response_body:
            self.__rate_result_list = []
            for item in response_body['rateResultList']:
                obj = RateResult()
                obj.parse_rsp_body(item)
                self.__rate_result_list.append(obj)
        if 'result' in response_body:
            self.__result = Result()
            self.__result.parse_rsp_body(response_body['result'])
