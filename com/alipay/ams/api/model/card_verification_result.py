import json
from com.alipay.ams.api.model.risk_three_ds_result import RiskThreeDSResult




class CardVerificationResult:
    def __init__(self):
        
        self.__authentication_type = None  # type: str
        self.__authentication_method = None  # type: str
        self.__cvv_result = None  # type: str
        self.__avs_result = None  # type: str
        self.__authorization_code = None  # type: str
        self.__three_ds_result = None  # type: RiskThreeDSResult
        

    @property
    def authentication_type(self):
        """
        Authentication type
        """
        return self.__authentication_type

    @authentication_type.setter
    def authentication_type(self, value):
        self.__authentication_type = value
    @property
    def authentication_method(self):
        """
        The authentication method that a merchant uses for a card payment
        """
        return self.__authentication_method

    @authentication_method.setter
    def authentication_method(self, value):
        self.__authentication_method = value
    @property
    def cvv_result(self):
        """
        The verification result of the card verification value (CVV)
        """
        return self.__cvv_result

    @cvv_result.setter
    def cvv_result(self, value):
        self.__cvv_result = value
    @property
    def avs_result(self):
        """
        The address verification result.
        """
        return self.__avs_result

    @avs_result.setter
    def avs_result(self, value):
        self.__avs_result = value
    @property
    def authorization_code(self):
        """
        The authorization code granted by the payment method provider for a successful 3D authentication.
        """
        return self.__authorization_code

    @authorization_code.setter
    def authorization_code(self, value):
        self.__authorization_code = value
    @property
    def three_ds_result(self):
        """Gets the three_ds_result of this CardVerificationResult.
        
        """
        return self.__three_ds_result

    @three_ds_result.setter
    def three_ds_result(self, value):
        self.__three_ds_result = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "authentication_type") and self.authentication_type is not None:
            params['authenticationType'] = self.authentication_type
        if hasattr(self, "authentication_method") and self.authentication_method is not None:
            params['authenticationMethod'] = self.authentication_method
        if hasattr(self, "cvv_result") and self.cvv_result is not None:
            params['cvvResult'] = self.cvv_result
        if hasattr(self, "avs_result") and self.avs_result is not None:
            params['avsResult'] = self.avs_result
        if hasattr(self, "authorization_code") and self.authorization_code is not None:
            params['authorizationCode'] = self.authorization_code
        if hasattr(self, "three_ds_result") and self.three_ds_result is not None:
            params['threeDSResult'] = self.three_ds_result
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'authenticationType' in response_body:
            self.__authentication_type = response_body['authenticationType']
        if 'authenticationMethod' in response_body:
            self.__authentication_method = response_body['authenticationMethod']
        if 'cvvResult' in response_body:
            self.__cvv_result = response_body['cvvResult']
        if 'avsResult' in response_body:
            self.__avs_result = response_body['avsResult']
        if 'authorizationCode' in response_body:
            self.__authorization_code = response_body['authorizationCode']
        if 'threeDSResult' in response_body:
            self.__three_ds_result = RiskThreeDSResult()
            self.__three_ds_result.parse_rsp_body(response_body['threeDSResult'])
