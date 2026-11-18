import json




class PaymentVerificationData:
    def __init__(self):
        
        self.__verify_request_id = None  # type: str
        self.__authentication_code = None  # type: str
        

    @property
    def verify_request_id(self):
        """Gets the verify_request_id of this PaymentVerificationData.
        
        """
        return self.__verify_request_id

    @verify_request_id.setter
    def verify_request_id(self, value):
        self.__verify_request_id = value
    @property
    def authentication_code(self):
        """Gets the authentication_code of this PaymentVerificationData.
        
        """
        return self.__authentication_code

    @authentication_code.setter
    def authentication_code(self, value):
        self.__authentication_code = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "verify_request_id") and self.verify_request_id is not None:
            params['verifyRequestId'] = self.verify_request_id
        if hasattr(self, "authentication_code") and self.authentication_code is not None:
            params['authenticationCode'] = self.authentication_code
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'verifyRequestId' in response_body:
            self.__verify_request_id = response_body['verifyRequestId']
        if 'authenticationCode' in response_body:
            self.__authentication_code = response_body['authenticationCode']
