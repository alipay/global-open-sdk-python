import json




class PaymentAttempt:
    def __init__(self):
        
        self.__attempt_at = None  # type: str
        self.__attempt_response = None  # type: str
        

    @property
    def attempt_at(self):
        """
        The initiation time of this payment attempt. ISO 8601 format.
        """
        return self.__attempt_at

    @attempt_at.setter
    def attempt_at(self, value):
        self.__attempt_at = value
    @property
    def attempt_response(self):
        """
        The result of the attempt. Maximum length: 64 characters.
        """
        return self.__attempt_response

    @attempt_response.setter
    def attempt_response(self, value):
        self.__attempt_response = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "attempt_at") and self.attempt_at is not None:
            params['attemptAt'] = self.attempt_at
        if hasattr(self, "attempt_response") and self.attempt_response is not None:
            params['attemptResponse'] = self.attempt_response
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'attemptAt' in response_body:
            self.__attempt_at = response_body['attemptAt']
        if 'attemptResponse' in response_body:
            self.__attempt_response = response_body['attemptResponse']
