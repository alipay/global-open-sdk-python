import json
from com.alipay.ams.api.model.result import Result
from com.alipay.ams.api.model.reserve_rule import ReserveRule



from com.alipay.ams.api.response.alipay_response import AlipayResponse

class AlipayInquireRuleListResponse(AlipayResponse):
    def __init__(self, rsp_body):
        super(AlipayResponse, self).__init__() 

        self.__result = None  # type: Result
        self.__has_more = None  # type: bool
        self.__rules = None  # type: [ReserveRule]
        self.parse_rsp_body(rsp_body) 


    @property
    def result(self):
        """Gets the result of this AlipayInquireRuleListResponse.
        
        """
        return self.__result

    @result.setter
    def result(self, value):
        self.__result = value
    @property
    def has_more(self):
        """
        Whether another page of rules is available. This field is false when rules is empty.
        """
        return self.__has_more

    @has_more.setter
    def has_more(self, value):
        self.__has_more = value
    @property
    def rules(self):
        """
        The reserve rules in descending ruleId order. An empty result is returned as an empty array.
        """
        return self.__rules

    @rules.setter
    def rules(self, value):
        self.__rules = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "result") and self.result is not None:
            params['result'] = self.result
        if hasattr(self, "has_more") and self.has_more is not None:
            params['hasMore'] = self.has_more
        if hasattr(self, "rules") and self.rules is not None:
            params['rules'] = self.rules
        return params


    def parse_rsp_body(self, response_body):
        response_body = super(AlipayInquireRuleListResponse, self).parse_rsp_body(response_body)
        if 'result' in response_body:
            self.__result = Result()
            self.__result.parse_rsp_body(response_body['result'])
        if 'hasMore' in response_body:
            self.__has_more = response_body['hasMore']
        if 'rules' in response_body:
            self.__rules = []
            for item in response_body['rules']:
                obj = ReserveRule()
                obj.parse_rsp_body(item)
                self.__rules.append(obj)
