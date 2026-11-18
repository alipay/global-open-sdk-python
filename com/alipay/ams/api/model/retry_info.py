import json
from com.alipay.ams.api.model.payment_attempt import PaymentAttempt




class RetryInfo:
    def __init__(self):
        
        self.__available_retries = None  # type: int
        self.__order_id = None  # type: str
        self.__payment_attempts = None  # type: [PaymentAttempt]
        

    @property
    def available_retries(self):
        """
        The remaining number of payment retry attempts. Only used in the PIX recurrence scenario.
        """
        return self.__available_retries

    @available_retries.setter
    def available_retries(self, value):
        self.__available_retries = value
    @property
    def order_id(self):
        """
        The order number for this subscription period. Only used in the PIX recurrence scenario. Maximum length: 32 characters.
        """
        return self.__order_id

    @order_id.setter
    def order_id(self, value):
        self.__order_id = value
    @property
    def payment_attempts(self):
        """
        Records of initiated attempts for the recurring payment. Maximum size: 4 elements.
        """
        return self.__payment_attempts

    @payment_attempts.setter
    def payment_attempts(self, value):
        self.__payment_attempts = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "available_retries") and self.available_retries is not None:
            params['availableRetries'] = self.available_retries
        if hasattr(self, "order_id") and self.order_id is not None:
            params['orderId'] = self.order_id
        if hasattr(self, "payment_attempts") and self.payment_attempts is not None:
            params['paymentAttempts'] = self.payment_attempts
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'availableRetries' in response_body:
            self.__available_retries = response_body['availableRetries']
        if 'orderId' in response_body:
            self.__order_id = response_body['orderId']
        if 'paymentAttempts' in response_body:
            self.__payment_attempts = []
            for item in response_body['paymentAttempts']:
                obj = PaymentAttempt()
                obj.parse_rsp_body(item)
                self.__payment_attempts.append(obj)
