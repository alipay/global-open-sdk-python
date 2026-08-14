import json
from com.alipay.ams.api.model.result import Result
from com.alipay.ams.api.model.card_transaction_lifecycle_detail import CardTransactionLifecycleDetail



from com.alipay.ams.api.response.alipay_response import AlipayResponse

class AlipayInquireCardTransactionLifecycleDetailResponse(AlipayResponse):
    def __init__(self, rsp_body):
        super(AlipayResponse, self).__init__() 

        self.__result = None  # type: Result
        self.__lifecycle = None  # type: CardTransactionLifecycleDetail
        self.parse_rsp_body(rsp_body) 


    @property
    def result(self):
        """Gets the result of this AlipayInquireCardTransactionLifecycleDetailResponse.
        
        """
        return self.__result

    @result.setter
    def result(self, value):
        self.__result = value
    @property
    def lifecycle(self):
        """Gets the lifecycle of this AlipayInquireCardTransactionLifecycleDetailResponse.
        
        """
        return self.__lifecycle

    @lifecycle.setter
    def lifecycle(self, value):
        self.__lifecycle = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "result") and self.result is not None:
            params['result'] = self.result
        if hasattr(self, "lifecycle") and self.lifecycle is not None:
            params['lifecycle'] = self.lifecycle
        return params


    def parse_rsp_body(self, response_body):
        response_body = super(AlipayInquireCardTransactionLifecycleDetailResponse, self).parse_rsp_body(response_body)
        if 'result' in response_body:
            self.__result = Result()
            self.__result.parse_rsp_body(response_body['result'])
        if 'lifecycle' in response_body:
            self.__lifecycle = CardTransactionLifecycleDetail()
            self.__lifecycle.parse_rsp_body(response_body['lifecycle'])
