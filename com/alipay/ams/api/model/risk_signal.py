import json




class RiskSignal:
    def __init__(self):
        
        self.__risk_code = None  # type: str
        self.__risk_reason = None  # type: str
        

    @property
    def risk_code(self):
        """
        The tag assigned by a merchant to a risky transaction.
        """
        return self.__risk_code

    @risk_code.setter
    def risk_code(self, value):
        self.__risk_code = value
    @property
    def risk_reason(self):
        """
        The reason why a transaction is identified as risky provided by a merchant.
        """
        return self.__risk_reason

    @risk_reason.setter
    def risk_reason(self, value):
        self.__risk_reason = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "risk_code") and self.risk_code is not None:
            params['riskCode'] = self.risk_code
        if hasattr(self, "risk_reason") and self.risk_reason is not None:
            params['riskReason'] = self.risk_reason
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'riskCode' in response_body:
            self.__risk_code = response_body['riskCode']
        if 'riskReason' in response_body:
            self.__risk_reason = response_body['riskReason']
