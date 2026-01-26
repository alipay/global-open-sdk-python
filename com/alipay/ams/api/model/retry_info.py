import json

from com.alipay.ams.api.model.payment_attempt import PaymentAttempt


class RetryInfo:
    def __init__(self):
        self.__available_retries = None # type: int
        self.__payment_attempts = None # type: list: PaymentAttempt


    @property
    def available_retries(self):
        return self.__available_retries

    @available_retries.setter
    def available_retries(self, value):
        self.__available_retries = value


    @property
    def payment_attempts(self):
        return self.__payment_attempts

    @payment_attempts.setter
    def payment_attempts(self, value):
        self.__payment_attempts = value


    def to_ams_dict(self):
        params = dict()
        if self.__available_retries:
            params['availableRetries'] = self.__available_retries
        if self.__payment_attempts:
            params['paymentAttempts'] = [i.to_ams_dict() for i in self.__payment_attempts]
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str):
            response_body = json.loads(response_body)
        if 'availableRetries' in response_body:
            self.__available_retries = response_body['availableRetries']
        if 'paymentAttempts' in response_body:
            self.__payment_attempts = [PaymentAttempt().parse_rsp_body(i) for i in response_body['paymentAttempts']]