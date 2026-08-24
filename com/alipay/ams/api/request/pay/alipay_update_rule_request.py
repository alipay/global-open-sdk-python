import json
from com.alipay.ams.api.model.payment_method_scope import PaymentMethodScope
from com.alipay.ams.api.model.rule_status import RuleStatus



from com.alipay.ams.api.request.alipay_request import AlipayRequest

class AlipayUpdateRuleRequest(AlipayRequest):
    def __init__(self):
        super(AlipayUpdateRuleRequest, self).__init__("/ams/api/v1/payments/reserve/updateRule") 

        self.__rule_id = None  # type: str
        self.__payment_method_scope = None  # type: PaymentMethodScope
        self.__ratio = None  # type: int
        self.__release_time = None  # type: str
        self.__retention_time = None  # type: int
        self.__rule_status = None  # type: RuleStatus
        

    @property
    def rule_id(self):
        """
        The Antom-assigned reserve rule identifier to update.
        """
        return self.__rule_id

    @rule_id.setter
    def rule_id(self, value):
        self.__rule_id = value
    @property
    def payment_method_scope(self):
        """Gets the payment_method_scope of this AlipayUpdateRuleRequest.
        
        """
        return self.__payment_method_scope

    @payment_method_scope.setter
    def payment_method_scope(self, value):
        self.__payment_method_scope = value
    @property
    def ratio(self):
        """
        The updated rolling reserve percentage. Omission or null leaves the field unchanged.
        """
        return self.__ratio

    @ratio.setter
    def ratio(self, value):
        self.__ratio = value
    @property
    def release_time(self):
        """
        The updated fixed release instant as a quoted ISO 8601 offset date-time. This field applies only to a stored FIXED_TIME rule. Omission or null leaves the field unchanged. A supplied instant must be from 3 through 180 days after the server time.
        """
        return self.__release_time

    @release_time.setter
    def release_time(self, value):
        self.__release_time = value
    @property
    def retention_time(self):
        """
        The updated rolling retention period in days. This field applies only to a stored INTERVAL_TIME rule. Omission or null leaves the field unchanged.
        """
        return self.__retention_time

    @retention_time.setter
    def retention_time(self, value):
        self.__retention_time = value
    @property
    def rule_status(self):
        """Gets the rule_status of this AlipayUpdateRuleRequest.
        
        """
        return self.__rule_status

    @rule_status.setter
    def rule_status(self, value):
        self.__rule_status = value


    def to_ams_json(self): 
        json_str = json.dumps(obj=self.to_ams_dict(), default=lambda o: o.to_ams_dict(), indent=3) 
        return json_str


    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "rule_id") and self.rule_id is not None:
            params['ruleId'] = self.rule_id
        if hasattr(self, "payment_method_scope") and self.payment_method_scope is not None:
            params['paymentMethodScope'] = self.payment_method_scope
        if hasattr(self, "ratio") and self.ratio is not None:
            params['ratio'] = self.ratio
        if hasattr(self, "release_time") and self.release_time is not None:
            params['releaseTime'] = self.release_time
        if hasattr(self, "retention_time") and self.retention_time is not None:
            params['retentionTime'] = self.retention_time
        if hasattr(self, "rule_status") and self.rule_status is not None:
            params['ruleStatus'] = self.rule_status
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'ruleId' in response_body:
            self.__rule_id = response_body['ruleId']
        if 'paymentMethodScope' in response_body:
            payment_method_scope_temp = PaymentMethodScope.value_of(response_body['paymentMethodScope'])
            self.__payment_method_scope = payment_method_scope_temp
        if 'ratio' in response_body:
            self.__ratio = response_body['ratio']
        if 'releaseTime' in response_body:
            self.__release_time = response_body['releaseTime']
        if 'retentionTime' in response_body:
            self.__retention_time = response_body['retentionTime']
        if 'ruleStatus' in response_body:
            rule_status_temp = RuleStatus.value_of(response_body['ruleStatus'])
            self.__rule_status = rule_status_temp
