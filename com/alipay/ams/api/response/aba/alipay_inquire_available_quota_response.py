import json
from com.alipay.ams.api.model.amount import Amount
from com.alipay.ams.api.model.result import Result



from com.alipay.ams.api.response.alipay_response import AlipayResponse

class AlipayInquireAvailableQuotaResponse(AlipayResponse):
    def __init__(self, rsp_body):
        super(AlipayResponse, self).__init__() 

        self.__available_quota = None  # type: Amount
        self.__result = None  # type: Result
        self.parse_rsp_body(rsp_body) 


    @property
    def available_quota(self):
        """Gets the available_quota of this AlipayInquireAvailableQuotaResponse.
        
        """
        return self.__available_quota

    @available_quota.setter
    def available_quota(self, value):
        self.__available_quota = value
    @property
    def result(self):
        """Gets the result of this AlipayInquireAvailableQuotaResponse.
        
        """
        return self.__result

    @result.setter
    def result(self, value):
        self.__result = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "available_quota") and self.available_quota is not None:
            params['availableQuota'] = self.available_quota
        if hasattr(self, "result") and self.result is not None:
            params['result'] = self.result
        return params


    def parse_rsp_body(self, response_body):
        response_body = super(AlipayInquireAvailableQuotaResponse, self).parse_rsp_body(response_body)
        if 'availableQuota' in response_body:
            self.__available_quota = Amount()
            self.__available_quota.parse_rsp_body(response_body['availableQuota'])
        if 'result' in response_body:
            self.__result = Result()
            self.__result.parse_rsp_body(response_body['result'])
