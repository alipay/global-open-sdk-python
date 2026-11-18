import json




class AgenticPaymentToken:
    def __init__(self):
        
        self.__token = None  # type: str
        self.__token_expiration_year = None  # type: str
        self.__token_expiration_month = None  # type: str
        self.__token_expiration = None  # type: str
        self.__status = None  # type: str
        self.__dynamic_data_type = None  # type: str
        self.__dynamic_data_value = None  # type: str
        

    @property
    def token(self):
        """
        One-time restricted payment credential (network token / DPAN). Required when result.resultStatus&#x3D;S.
        """
        return self.__token

    @token.setter
    def token(self, value):
        self.__token = value
    @property
    def token_expiration_year(self):
        """
        Four-digit year YYYY. Required for successful Visa/Mastercard CARD responses; omitted for A+.
        """
        return self.__token_expiration_year

    @token_expiration_year.setter
    def token_expiration_year(self, value):
        self.__token_expiration_year = value
    @property
    def token_expiration_month(self):
        """
        Two-digit month MM, from 01 to 12. Required for successful Visa/Mastercard CARD responses; omitted for A+.
        """
        return self.__token_expiration_month

    @token_expiration_month.setter
    def token_expiration_month(self, value):
        self.__token_expiration_month = value
    @property
    def token_expiration(self):
        """
        Credential expiration time, required when result.resultStatus&#x3D;S. Wire value is an RFC 3339 / ISO 8601 string with a timezone, up to 64 characters; it is not converted to a date object.
        """
        return self.__token_expiration

    @token_expiration.setter
    def token_expiration(self, value):
        self.__token_expiration = value
    @property
    def status(self):
        """
        Optional credential availability snapshot. The only public value is ACTIVE. Expiration is expressed by tokenExpiration; EXPIRED, SUSPENDED and REVOKED are not returned. The credential cannot be used after expiration or restored to ACTIVE. Unknown or unmappable channel status, or inability to confirm usability, produces PROCESS_FAIL/F without paymentToken. May be omitted when successful issuance guarantees usability. Supported values (case-sensitive): ACTIVE.
        """
        return self.__status

    @status.setter
    def status(self, value):
        self.__status = value
    @property
    def dynamic_data_type(self):
        """
        Dynamic cryptogram type, required for successful Visa/Mastercard responses and omitted for A+. Closed values: DAVV, TAVV, CARD_APPLICATION_CRYPTOGRAM_SHORT_FORM, DYNAMIC_CARD_SECURITY_CODE. Visa uses DAVV/TAVV; Mastercard uses the other two values. Missing or unmappable channel dynamic data produces PROCESS_FAIL/F without paymentToken. Supported values (case-sensitive): DAVV, TAVV, CARD_APPLICATION_CRYPTOGRAM_SHORT_FORM, DYNAMIC_CARD_SECURITY_CODE.
        """
        return self.__dynamic_data_type

    @dynamic_data_type.setter
    def dynamic_data_type(self, value):
        self.__dynamic_data_type = value
    @property
    def dynamic_data_value(self):
        """
        Dynamic cryptogram value, required for successful Visa/Mastercard responses and omitted for A+. Missing channel dynamic data produces PROCESS_FAIL/F without paymentToken.
        """
        return self.__dynamic_data_value

    @dynamic_data_value.setter
    def dynamic_data_value(self, value):
        self.__dynamic_data_value = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "token") and self.token is not None:
            params['token'] = self.token
        if hasattr(self, "token_expiration_year") and self.token_expiration_year is not None:
            params['tokenExpirationYear'] = self.token_expiration_year
        if hasattr(self, "token_expiration_month") and self.token_expiration_month is not None:
            params['tokenExpirationMonth'] = self.token_expiration_month
        if hasattr(self, "token_expiration") and self.token_expiration is not None:
            params['tokenExpiration'] = self.token_expiration
        if hasattr(self, "status") and self.status is not None:
            params['status'] = self.status
        if hasattr(self, "dynamic_data_type") and self.dynamic_data_type is not None:
            params['dynamicDataType'] = self.dynamic_data_type
        if hasattr(self, "dynamic_data_value") and self.dynamic_data_value is not None:
            params['dynamicDataValue'] = self.dynamic_data_value
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'token' in response_body:
            self.__token = response_body['token']
        if 'tokenExpirationYear' in response_body:
            self.__token_expiration_year = response_body['tokenExpirationYear']
        if 'tokenExpirationMonth' in response_body:
            self.__token_expiration_month = response_body['tokenExpirationMonth']
        if 'tokenExpiration' in response_body:
            self.__token_expiration = response_body['tokenExpiration']
        if 'status' in response_body:
            self.__status = response_body['status']
        if 'dynamicDataType' in response_body:
            self.__dynamic_data_type = response_body['dynamicDataType']
        if 'dynamicDataValue' in response_body:
            self.__dynamic_data_value = response_body['dynamicDataValue']
