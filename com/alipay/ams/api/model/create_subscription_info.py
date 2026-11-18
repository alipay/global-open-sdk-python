import json
from com.alipay.ams.api.model.amount import Amount
from com.alipay.ams.api.model.amount import Amount




class CreateSubscriptionInfo:
    def __init__(self):
        
        self.__allow_retry = None  # type: bool
        self.__retry_mode = None  # type: str
        self.__max_amount_floor = None  # type: Amount
        self.__fixed_amount = None  # type: Amount
        

    @property
    def allow_retry(self):
        """
        Whether to allow retry for PIX recurrence payments. Defaults to false when not provided.
        """
        return self.__allow_retry

    @allow_retry.setter
    def allow_retry(self, value):
        self.__allow_retry = value
    @property
    def retry_mode(self):
        """
        The retry mode. Valid values are MANUAL and AUTOMATIC. Defaults to MANUAL when allowRetry is true. Maximum length: 9 characters.
        """
        return self.__retry_mode

    @retry_mode.setter
    def retry_mode(self, value):
        self.__retry_mode = value
    @property
    def max_amount_floor(self):
        """Gets the max_amount_floor of this CreateSubscriptionInfo.
        
        """
        return self.__max_amount_floor

    @max_amount_floor.setter
    def max_amount_floor(self, value):
        self.__max_amount_floor = value
    @property
    def fixed_amount(self):
        """Gets the fixed_amount of this CreateSubscriptionInfo.
        
        """
        return self.__fixed_amount

    @fixed_amount.setter
    def fixed_amount(self, value):
        self.__fixed_amount = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "allow_retry") and self.allow_retry is not None:
            params['allowRetry'] = self.allow_retry
        if hasattr(self, "retry_mode") and self.retry_mode is not None:
            params['retryMode'] = self.retry_mode
        if hasattr(self, "max_amount_floor") and self.max_amount_floor is not None:
            params['maxAmountFloor'] = self.max_amount_floor
        if hasattr(self, "fixed_amount") and self.fixed_amount is not None:
            params['fixedAmount'] = self.fixed_amount
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'allowRetry' in response_body:
            self.__allow_retry = response_body['allowRetry']
        if 'retryMode' in response_body:
            self.__retry_mode = response_body['retryMode']
        if 'maxAmountFloor' in response_body:
            self.__max_amount_floor = Amount()
            self.__max_amount_floor.parse_rsp_body(response_body['maxAmountFloor'])
        if 'fixedAmount' in response_body:
            self.__fixed_amount = Amount()
            self.__fixed_amount.parse_rsp_body(response_body['fixedAmount'])
