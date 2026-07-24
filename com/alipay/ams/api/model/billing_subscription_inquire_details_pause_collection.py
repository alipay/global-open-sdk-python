import json




class BillingSubscriptionInquireDetailsPauseCollection:
    def __init__(self):
        
        self.__behavior = None  # type: str
        self.__resumes_at = None  # type: str
        self.__paused_at = None  # type: str
        self.__reason_code = None  # type: str
        

    @property
    def behavior(self):
        """
        The behavior. Maximum length: 19 characters.
        """
        return self.__behavior

    @behavior.setter
    def behavior(self, value):
        self.__behavior = value
    @property
    def resumes_at(self):
        """
        The resumes at.
        """
        return self.__resumes_at

    @resumes_at.setter
    def resumes_at(self, value):
        self.__resumes_at = value
    @property
    def paused_at(self):
        """
        The paused at.
        """
        return self.__paused_at

    @paused_at.setter
    def paused_at(self, value):
        self.__paused_at = value
    @property
    def reason_code(self):
        """
        The reason code. Maximum length: 64 characters.
        """
        return self.__reason_code

    @reason_code.setter
    def reason_code(self, value):
        self.__reason_code = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "behavior") and self.behavior is not None:
            params['behavior'] = self.behavior
        if hasattr(self, "resumes_at") and self.resumes_at is not None:
            params['resumesAt'] = self.resumes_at
        if hasattr(self, "paused_at") and self.paused_at is not None:
            params['pausedAt'] = self.paused_at
        if hasattr(self, "reason_code") and self.reason_code is not None:
            params['reasonCode'] = self.reason_code
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'behavior' in response_body:
            self.__behavior = response_body['behavior']
        if 'resumesAt' in response_body:
            self.__resumes_at = response_body['resumesAt']
        if 'pausedAt' in response_body:
            self.__paused_at = response_body['pausedAt']
        if 'reasonCode' in response_body:
            self.__reason_code = response_body['reasonCode']
