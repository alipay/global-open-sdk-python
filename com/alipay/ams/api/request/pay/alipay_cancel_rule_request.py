import json



from com.alipay.ams.api.request.alipay_request import AlipayRequest

class AlipayCancelRuleRequest(AlipayRequest):
    def __init__(self):
        super(AlipayCancelRuleRequest, self).__init__("/ams/api/v1/payments/reserve/cancelRule") 

        self.__rule_id = None  # type: str
        

    @property
    def rule_id(self):
        """
        The Antom-assigned reserve rule identifier to cancel.
        """
        return self.__rule_id

    @rule_id.setter
    def rule_id(self, value):
        self.__rule_id = value


    def to_ams_json(self): 
        json_str = json.dumps(obj=self.to_ams_dict(), default=lambda o: o.to_ams_dict(), indent=3) 
        return json_str


    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "rule_id") and self.rule_id is not None:
            params['ruleId'] = self.rule_id
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'ruleId' in response_body:
            self.__rule_id = response_body['ruleId']
