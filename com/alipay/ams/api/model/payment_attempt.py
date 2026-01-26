import json


class PaymentAttempt:
    def __init__(self):
        self.__attemptAt = None  # type: str
        self.__attempt_response = None  # type: str


    @property
    def attemptAt(self):
        return self.__attemptAt

    @attemptAt.setter
    def attemptAt(self, value):
        self.__attemptAt = value
        
    @property
    def attempt_response(self):
        return self.__attempt_response
    @attempt_response.setter
    def attempt_response(self, value):
        self.__attempt_response = value

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "attemptAt") and self.attemptAt is not None:
            params['attemptAt'] = self.attemptAt
        if hasattr(self, "attempt_response") and self.attempt_response is not None:
            params['attempt_response'] = self.attempt_response
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str):
            response_body = json.loads(response_body)
        if 'attemptAt' in response_body:
            self.__attemptAt = response_body['attemptAt']
        if 'attempt_response' in response_body:
            self.__attempt_response = response_body['attempt_response']