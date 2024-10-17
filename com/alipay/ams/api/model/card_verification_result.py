from com.alipay.ams.api.model.three_ds_result import ThreeDSResult


class CardVerificationResult:
    def __init__(self):
        self.__authentication_type = None
        self.__authentication_method = None
        self.__cvv_result = None
        self.__avs_result = None
        self.__authorization_code = None
        self.__three_d_s_result = None #type: ThreeDSResult

    @property
    def authentication_type(self):
        return self.__authentication_type

    @authentication_type.setter
    def authentication_type(self, value):
        self.__authentication_type = value

    @property
    def authentication_method(self):
        return self.__authentication_method

    @authentication_method.setter
    def authentication_method(self, value):
        self.__authentication_method = value

    @property
    def cvv_result(self):
        return self.__cvv_result

    @cvv_result.setter
    def cvv_result(self, value):
        self.__cvv_result = value

    @property
    def avs_result(self):
        return self.__avs_result

    @avs_result.setter
    def avs_result(self, value):
        self.__avs_result = value

    @property
    def authorization_code(self):
        return self.__authorization_code

    @authorization_code.setter
    def authorization_code(self, value):
        self.__authorization_code = value

    @property
    def three_d_s_result(self):
        return self.__three_d_s_result

    @three_d_s_result.setter
    def three_d_s_result(self, value):
        self.__three_d_s_result = value


    def to_ams_dict(self):
        params = dict()
        if self.__authentication_type is not None:
            params['authenticationType'] = self.__authentication_type
        if self.__authentication_method is not None:
            params['authenticationMethod'] = self.__authentication_method
        if self.__cvv_result is not None:
            params['cvvResult'] = self.__cvv_result
        if self.__avs_result is not None:
            params['avsResult'] = self.__avs_result
        if self.__authorization_code is not None:
            params['authorizationCode'] = self.__authorization_code
        if self.__three_d_s_result is not None:
            params['threeDSResult'] = self.__three_d_s_result
        return params