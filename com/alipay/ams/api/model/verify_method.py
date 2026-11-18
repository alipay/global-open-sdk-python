import json




class VerifyMethod:
    def __init__(self):
        
        self.__verify_method_type = None  # type: str
        self.__otp_value = None  # type: str
        

    @property
    def verify_method_type(self):
        """Gets the verify_method_type of this VerifyMethod.
        
        """
        return self.__verify_method_type

    @verify_method_type.setter
    def verify_method_type(self, value):
        self.__verify_method_type = value
    @property
    def otp_value(self):
        """Gets the otp_value of this VerifyMethod.
        
        """
        return self.__otp_value

    @otp_value.setter
    def otp_value(self, value):
        self.__otp_value = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "verify_method_type") and self.verify_method_type is not None:
            params['verifyMethodType'] = self.verify_method_type
        if hasattr(self, "otp_value") and self.otp_value is not None:
            params['otpValue'] = self.otp_value
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'verifyMethodType' in response_body:
            self.__verify_method_type = response_body['verifyMethodType']
        if 'otpValue' in response_body:
            self.__otp_value = response_body['otpValue']
