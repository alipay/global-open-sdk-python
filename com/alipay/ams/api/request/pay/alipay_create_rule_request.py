import json
from com.alipay.ams.api.model.funds_type import FundsType
from com.alipay.ams.api.model.take_type import TakeType
from com.alipay.ams.api.model.payment_method_scope import PaymentMethodScope
from com.alipay.ams.api.model.release_type import ReleaseType



from com.alipay.ams.api.request.alipay_request import AlipayRequest

class AlipayCreateRuleRequest(AlipayRequest):
    def __init__(self):
        super(AlipayCreateRuleRequest, self).__init__("/ams/api/v1/payments/reserve/createRule") 

        self.__funds_type = None  # type: FundsType
        self.__take_type = None  # type: TakeType
        self.__payment_method_scope = None  # type: PaymentMethodScope
        self.__ratio = None  # type: int
        self.__release_type = None  # type: ReleaseType
        self.__release_time = None  # type: str
        self.__retention_time = None  # type: int
        

    @property
    def funds_type(self):
        """Gets the funds_type of this AlipayCreateRuleRequest.
        
        """
        return self.__funds_type

    @funds_type.setter
    def funds_type(self, value):
        self.__funds_type = value
    @property
    def take_type(self):
        """Gets the take_type of this AlipayCreateRuleRequest.
        
        """
        return self.__take_type

    @take_type.setter
    def take_type(self, value):
        self.__take_type = value
    @property
    def payment_method_scope(self):
        """Gets the payment_method_scope of this AlipayCreateRuleRequest.
        
        """
        return self.__payment_method_scope

    @payment_method_scope.setter
    def payment_method_scope(self, value):
        self.__payment_method_scope = value
    @property
    def ratio(self):
        """
        The rolling reserve percentage. An integer from 1 through 100.
        """
        return self.__ratio

    @ratio.setter
    def ratio(self, value):
        self.__ratio = value
    @property
    def release_type(self):
        """Gets the release_type of this AlipayCreateRuleRequest.
        
        """
        return self.__release_type

    @release_type.setter
    def release_type(self, value):
        self.__release_type = value
    @property
    def release_time(self):
        """
        The fixed release instant as a quoted ISO 8601 offset date-time. Required only when releaseType is FIXED_TIME. The parsed instant must be from 3 through 180 days after the server time. Do not provide this field when releaseType is INTERVAL_TIME.
        """
        return self.__release_time

    @release_time.setter
    def release_time(self, value):
        self.__release_time = value
    @property
    def retention_time(self):
        """
        The rolling retention period in days. Required only when releaseType is INTERVAL_TIME. Do not provide this field when releaseType is FIXED_TIME.
        """
        return self.__retention_time

    @retention_time.setter
    def retention_time(self, value):
        self.__retention_time = value


    def to_ams_json(self): 
        json_str = json.dumps(obj=self.to_ams_dict(), default=lambda o: o.to_ams_dict(), indent=3) 
        return json_str


    def to_ams_dict(self):
        params = dict()
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
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
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
