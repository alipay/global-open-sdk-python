import json
from com.alipay.ams.api.model.result import Result



from com.alipay.ams.api.response.alipay_response import AlipayResponse

class AlipaySettleResponse(AlipayResponse):
    def __init__(self, rsp_body):
        super(AlipayResponse, self).__init__() 

        self.__result = None  # type: Result
        self.__settlement_request_id = None  # type: str
        self.__settlement_id = None  # type: str
        self.parse_rsp_body(rsp_body) 


    @property
    def result(self):
        """Gets the result of this AlipaySettleResponse.
        
        """
        return self.__result

    @result.setter
    def result(self, value):
        self.__result = value
    @property
    def settlement_request_id(self):
        """
        The unique ID that is assigned by the marketplace to identify a settlement request.    More information:  Maximum length: 64 characters
        """
        return self.__settlement_request_id

    @settlement_request_id.setter
    def settlement_request_id(self, value):
        self.__settlement_request_id = value
    @property
    def settlement_id(self):
        """
        The unique ID that is assigned by Antom to identify a settlement.    More information:  Maximum length: 64 characters
        """
        return self.__settlement_id

    @settlement_id.setter
    def settlement_id(self, value):
        self.__settlement_id = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "result") and self.result is not None:
            params['result'] = self.result
        if hasattr(self, "settlement_request_id") and self.settlement_request_id is not None:
            params['settlementRequestId'] = self.settlement_request_id
        if hasattr(self, "settlement_id") and self.settlement_id is not None:
            params['settlementId'] = self.settlement_id
        return params


    def parse_rsp_body(self, response_body):
        response_body = super(AlipaySettleResponse, self).parse_rsp_body(response_body)
        if 'result' in response_body:
            self.__result = Result()
            self.__result.parse_rsp_body(response_body['result'])
        if 'settlementRequestId' in response_body:
            self.__settlement_request_id = response_body['settlementRequestId']
        if 'settlementId' in response_body:
            self.__settlement_id = response_body['settlementId']
