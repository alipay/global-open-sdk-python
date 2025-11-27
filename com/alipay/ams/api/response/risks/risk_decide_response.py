from com.alipay.ams.api.response.alipay_response import AlipayResponse


class RiskDecideResponse(AlipayResponse):
    def __init__(self, rsp_body):
        super(RiskDecideResponse, self).__init__()
        self.__decision = None
        self.__authentication_decision = None
        self.__parse_rsp_body(rsp_body)

    @property
    def decision(self):
        return self.__decision

    @decision.setter
    def decision(self, decision):
        self.__decision = decision

    @property
    def authentication_decision(self):
        return self.__authentication_decision

    @authentication_decision.setter
    def authentication_decision(self, authentication_decision):
        self.__authentication_decision = authentication_decision

    def __parse_rsp_body(self, rsp_body):
        response = super(RiskDecideResponse, self).parse_rsp_body(rsp_body)
        if "decision" in response:
            self.decision = response["decision"]
        if "authentication_decision" in response:
            self.authentication_decision = response["authenticationDecision"]
