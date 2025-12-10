import json
from com.alipay.ams.api.model.result import Result



from com.alipay.ams.api.response.alipay_response import AlipayResponse

class AlipaySettlementInfoUpdateResponse(AlipayResponse):
    def __init__(self, rsp_body):
        super(AlipayResponse, self).__init__() 

        self.__result = None  # type: Result
        self.__update_status = None  # type: str
        self.parse_rsp_body(rsp_body) 


    @property
    def result(self):
        """Gets the result of this AlipaySettlementInfoUpdateResponse.
        
        """
        return self.__result

    @result.setter
    def result(self, value):
        self.__result = value
    @property
    def update_status(self):
        """
        The update status of the settlement information. The value of this parameter is fixed to PROCESSING.   Get the settlement information update result from the notifyUpdate and inquireUpdate interfaces.   This parameter is returned when the value of result.resultStatus is S.    More information:  Maximum length: 64 characters
        """
        return self.__update_status

    @update_status.setter
    def update_status(self, value):
        self.__update_status = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "result") and self.result is not None:
            params['result'] = self.result
        if hasattr(self, "update_status") and self.update_status is not None:
            params['updateStatus'] = self.update_status
        return params


    def parse_rsp_body(self, response_body):
        response_body = super(AlipaySettlementInfoUpdateResponse, self).parse_rsp_body(response_body)
        if 'result' in response_body:
            self.__result = Result()
            self.__result.parse_rsp_body(response_body['result'])
        if 'updateStatus' in response_body:
            self.__update_status = response_body['updateStatus']
