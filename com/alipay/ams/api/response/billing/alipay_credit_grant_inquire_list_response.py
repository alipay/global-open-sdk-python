import json
from com.alipay.ams.api.model.result import Result
from com.alipay.ams.api.model.credit_grant import CreditGrant



from com.alipay.ams.api.response.alipay_response import AlipayResponse

class AlipayCreditGrantInquireListResponse(AlipayResponse):
    def __init__(self, rsp_body):
        super(AlipayResponse, self).__init__() 

        self.__result = None  # type: Result
        self.__credit_grants = None  # type: CreditGrant
        self.parse_rsp_body(rsp_body) 


    @property
    def result(self):
        """Gets the result of this AlipayCreditGrantInquireListResponse.
        
        """
        return self.__result

    @result.setter
    def result(self, value):
        self.__result = value
    @property
    def credit_grants(self):
        """Gets the credit_grants of this AlipayCreditGrantInquireListResponse.
        
        """
        return self.__credit_grants

    @credit_grants.setter
    def credit_grants(self, value):
        self.__credit_grants = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "result") and self.result is not None:
            params['result'] = self.result
        if hasattr(self, "credit_grants") and self.credit_grants is not None:
            params['creditGrants'] = self.credit_grants
        return params


    def parse_rsp_body(self, response_body):
        response_body = super(AlipayCreditGrantInquireListResponse, self).parse_rsp_body(response_body)
        if 'result' in response_body:
            self.__result = Result()
            self.__result.parse_rsp_body(response_body['result'])
        if 'creditGrants' in response_body:
            self.__credit_grants = CreditGrant()
            self.__credit_grants.parse_rsp_body(response_body['creditGrants'])
