import json




class PopRiskDecisionResultInfo:
    def __init__(self):
        
        self.__risk_auth_decision = None  # type: str
        self.__risk_decision = None  # type: str
        self.__post_risk_decision = None  # type: str
        

    @property
    def risk_auth_decision(self):
        """
        The risk decision that is related to the authorization of the payment.
        """
        return self.__risk_auth_decision

    @risk_auth_decision.setter
    def risk_auth_decision(self, value):
        self.__risk_auth_decision = value
    @property
    def risk_decision(self):
        """
        The risk decision for the payment.
        """
        return self.__risk_decision

    @risk_decision.setter
    def risk_decision(self, value):
        self.__risk_decision = value
    @property
    def post_risk_decision(self):
        """
        The post-authorization risk decision result. Valid values are:  ACCEPT: The post-authorization risk review is passed. The merchant can continue to capture the payment or fulfill the order. REVIEW: The post-authorization risk review recommends a manual review. REJECT: The post-authorization risk review is rejected. Cancel the order.  Note: This field is returned when the merchant calls the post-authorization risk review interface and the interface returns a non-empty result within the time limit. When the interface times out, returns null, or is not called, this field is not returned and no post-authorization risk review is deemed to have occurred.  More information:  Maximum length: 6 characters
        """
        return self.__post_risk_decision

    @post_risk_decision.setter
    def post_risk_decision(self, value):
        self.__post_risk_decision = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "risk_auth_decision") and self.risk_auth_decision is not None:
            params['riskAuthDecision'] = self.risk_auth_decision
        if hasattr(self, "risk_decision") and self.risk_decision is not None:
            params['riskDecision'] = self.risk_decision
        if hasattr(self, "post_risk_decision") and self.post_risk_decision is not None:
            params['postRiskDecision'] = self.post_risk_decision
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'riskAuthDecision' in response_body:
            self.__risk_auth_decision = response_body['riskAuthDecision']
        if 'riskDecision' in response_body:
            self.__risk_decision = response_body['riskDecision']
        if 'postRiskDecision' in response_body:
            self.__post_risk_decision = response_body['postRiskDecision']
