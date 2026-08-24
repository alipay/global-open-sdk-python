import json
from com.alipay.ams.api.model.result import Result
from com.alipay.ams.api.model.funds_type import FundsType
from com.alipay.ams.api.model.take_type import TakeType
from com.alipay.ams.api.model.payment_method_scope import PaymentMethodScope
from com.alipay.ams.api.model.release_type import ReleaseType
from com.alipay.ams.api.model.rule_status import RuleStatus



from com.alipay.ams.api.response.alipay_response import AlipayResponse

class AlipayCancelRuleResponse(AlipayResponse):
    def __init__(self, rsp_body):
        super(AlipayResponse, self).__init__() 

        self.__result = None  # type: Result
        self.__rule_id = None  # type: str
        self.__merchant_id = None  # type: str
        self.__funds_type = None  # type: FundsType
        self.__take_type = None  # type: TakeType
        self.__payment_method_scope = None  # type: PaymentMethodScope
        self.__ratio = None  # type: int
        self.__release_type = None  # type: ReleaseType
        self.__release_time = None  # type: str
        self.__retention_time = None  # type: int
        self.__rule_status = None  # type: RuleStatus
        self.__create_time = None  # type: str
        self.__update_time = None  # type: str
        self.parse_rsp_body(rsp_body) 


    @property
    def result(self):
        """Gets the result of this AlipayCancelRuleResponse.
        
        """
        return self.__result

    @result.setter
    def result(self, value):
        self.__result = value
    @property
    def rule_id(self):
        """
        The Antom-assigned positive numeric reserve rule identifier. Save and return this value unchanged for updates, cancellation, and cursor pagination. Returned only when result.resultCode is SUCCESS.
        """
        return self.__rule_id

    @rule_id.setter
    def rule_id(self, value):
        self.__rule_id = value
    @property
    def merchant_id(self):
        """
        The ID of the merchant that owns the reserve rule. Returned only when result.resultCode is SUCCESS.
        """
        return self.__merchant_id

    @merchant_id.setter
    def merchant_id(self, value):
        self.__merchant_id = value
    @property
    def funds_type(self):
        """Gets the funds_type of this AlipayCancelRuleResponse.
        
        """
        return self.__funds_type

    @funds_type.setter
    def funds_type(self, value):
        self.__funds_type = value
    @property
    def take_type(self):
        """Gets the take_type of this AlipayCancelRuleResponse.
        
        """
        return self.__take_type

    @take_type.setter
    def take_type(self, value):
        self.__take_type = value
    @property
    def payment_method_scope(self):
        """Gets the payment_method_scope of this AlipayCancelRuleResponse.
        
        """
        return self.__payment_method_scope

    @payment_method_scope.setter
    def payment_method_scope(self, value):
        self.__payment_method_scope = value
    @property
    def ratio(self):
        """
        The rolling reserve percentage. Returned when takeType is ROLLING and result.resultCode is SUCCESS.
        """
        return self.__ratio

    @ratio.setter
    def ratio(self, value):
        self.__ratio = value
    @property
    def release_type(self):
        """Gets the release_type of this AlipayCancelRuleResponse.
        
        """
        return self.__release_type

    @release_type.setter
    def release_type(self, value):
        self.__release_type = value
    @property
    def release_time(self):
        """
        The fixed release instant as an ISO 8601 UTC string, for example 2026-12-31T16:00:00Z. Returned when releaseType is FIXED_TIME and result.resultCode is SUCCESS.
        """
        return self.__release_time

    @release_time.setter
    def release_time(self, value):
        self.__release_time = value
    @property
    def retention_time(self):
        """
        The rolling retention period in days. Returned when releaseType is INTERVAL_TIME and result.resultCode is SUCCESS.
        """
        return self.__retention_time

    @retention_time.setter
    def retention_time(self, value):
        self.__retention_time = value
    @property
    def rule_status(self):
        """Gets the rule_status of this AlipayCancelRuleResponse.
        
        """
        return self.__rule_status

    @rule_status.setter
    def rule_status(self, value):
        self.__rule_status = value
    @property
    def create_time(self):
        """
        The rule creation time as an ISO 8601 UTC string. Returned only when result.resultCode is SUCCESS.
        """
        return self.__create_time

    @create_time.setter
    def create_time(self, value):
        self.__create_time = value
    @property
    def update_time(self):
        """
        The rule last-update time as an ISO 8601 UTC string. Returned only when result.resultCode is SUCCESS.
        """
        return self.__update_time

    @update_time.setter
    def update_time(self, value):
        self.__update_time = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "result") and self.result is not None:
            params['result'] = self.result
        if hasattr(self, "rule_id") and self.rule_id is not None:
            params['ruleId'] = self.rule_id
        if hasattr(self, "merchant_id") and self.merchant_id is not None:
            params['merchantId'] = self.merchant_id
        if hasattr(self, "funds_type") and self.funds_type is not None:
            params['fundsType'] = self.funds_type
        if hasattr(self, "take_type") and self.take_type is not None:
            params['takeType'] = self.take_type
        if hasattr(self, "payment_method_scope") and self.payment_method_scope is not None:
            params['paymentMethodScope'] = self.payment_method_scope
        if hasattr(self, "ratio") and self.ratio is not None:
            params['ratio'] = self.ratio
        if hasattr(self, "release_type") and self.release_type is not None:
            params['releaseType'] = self.release_type
        if hasattr(self, "release_time") and self.release_time is not None:
            params['releaseTime'] = self.release_time
        if hasattr(self, "retention_time") and self.retention_time is not None:
            params['retentionTime'] = self.retention_time
        if hasattr(self, "rule_status") and self.rule_status is not None:
            params['ruleStatus'] = self.rule_status
        if hasattr(self, "create_time") and self.create_time is not None:
            params['createTime'] = self.create_time
        if hasattr(self, "update_time") and self.update_time is not None:
            params['updateTime'] = self.update_time
        return params


    def parse_rsp_body(self, response_body):
        response_body = super(AlipayCancelRuleResponse, self).parse_rsp_body(response_body)
        if 'result' in response_body:
            self.__result = Result()
            self.__result.parse_rsp_body(response_body['result'])
        if 'ruleId' in response_body:
            self.__rule_id = response_body['ruleId']
        if 'merchantId' in response_body:
            self.__merchant_id = response_body['merchantId']
        if 'fundsType' in response_body:
            funds_type_temp = FundsType.value_of(response_body['fundsType'])
            self.__funds_type = funds_type_temp
        if 'takeType' in response_body:
            take_type_temp = TakeType.value_of(response_body['takeType'])
            self.__take_type = take_type_temp
        if 'paymentMethodScope' in response_body:
            payment_method_scope_temp = PaymentMethodScope.value_of(response_body['paymentMethodScope'])
            self.__payment_method_scope = payment_method_scope_temp
        if 'ratio' in response_body:
            self.__ratio = response_body['ratio']
        if 'releaseType' in response_body:
            release_type_temp = ReleaseType.value_of(response_body['releaseType'])
            self.__release_type = release_type_temp
        if 'releaseTime' in response_body:
            self.__release_time = response_body['releaseTime']
        if 'retentionTime' in response_body:
            self.__retention_time = response_body['retentionTime']
        if 'ruleStatus' in response_body:
            rule_status_temp = RuleStatus.value_of(response_body['ruleStatus'])
            self.__rule_status = rule_status_temp
        if 'createTime' in response_body:
            self.__create_time = response_body['createTime']
        if 'updateTime' in response_body:
            self.__update_time = response_body['updateTime']
