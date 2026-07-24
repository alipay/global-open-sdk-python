import json
from com.alipay.ams.api.model.result import Result
from com.alipay.ams.api.model.credit_grant import CreditGrant



from com.alipay.ams.api.response.alipay_response import AlipayResponse

class AlipayCreditGrantVoidResponse(AlipayResponse):
    def __init__(self, rsp_body):
        super(AlipayResponse, self).__init__() 

        self.__result = None  # type: Result
        self.__credit_grant = None  # type: CreditGrant
        self.parse_rsp_body(rsp_body) 


    @property
    def result(self):
        """Gets the result of this AlipayCreditGrantVoidResponse.
        
        """
        return self.__result

    @result.setter
    def result(self, value):
        self.__result = value
    @property
    def credit_grant(self):
        """Gets the credit_grant of this AlipayCreditGrantVoidResponse.
        
        """
        return self.__credit_grant

    @credit_grant.setter
    def credit_grant(self, value):
        self.__credit_grant = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "result") and self.result is not None:
            params['result'] = self.result
        if hasattr(self, "credit_grant") and self.credit_grant is not None:
            params['creditGrant'] = self.credit_grant
        return params


    def parse_rsp_body(self, response_body):
        response_body = super(AlipayCreditGrantVoidResponse, self).parse_rsp_body(response_body)
        if 'result' in response_body:
            self.__result = Result()
            self.__result.parse_rsp_body(response_body['result'])
        if 'creditGrant' in response_body:
            self.__credit_grant = CreditGrant()
            self.__credit_grant.parse_rsp_body(response_body['creditGrant'])
