import json



from com.alipay.ams.api.request.alipay_request import AlipayRequest

class AlipayTaxUpdateRegistrationPeriodRequest(AlipayRequest):
    def __init__(self):
        super(AlipayTaxUpdateRegistrationPeriodRequest, self).__init__("/ams/api/v1/tax/updateRegistrationPeriod") 

        self.__registration_update_period_request_id = None  # type: str
        self.__tax_registration_id = None  # type: str
        self.__active_from = None  # type: str
        self.__expire_at = None  # type: str
        

    @property
    def registration_update_period_request_id(self):
        """
        The unique ID assigned by a merchant to identify a tax registration period update request. Maximum length: 32 characters. Note: See documentation for details.
        """
        return self.__registration_update_period_request_id

    @registration_update_period_request_id.setter
    def registration_update_period_request_id(self, value):
        self.__registration_update_period_request_id = value
    @property
    def tax_registration_id(self):
        """
        The unique ID assigned by Antom to identify a tax registration. Maximum length: 64 characters.
        """
        return self.__tax_registration_id

    @tax_registration_id.setter
    def tax_registration_id(self, value):
        self.__tax_registration_id = value
    @property
    def active_from(self):
        """
        The new activation time for a SCHEDULED registration. The value must be later than the current time. Maximum length: 32 characters.
        """
        return self.__active_from

    @active_from.setter
    def active_from(self, value):
        self.__active_from = value
    @property
    def expire_at(self):
        """
        The new expiration time for an ACTIVE or SCHEDULED registration. The value must be later than the current time and, for a scheduled registration, later than the effective activeFrom. Maximum length: 32 characters.
        """
        return self.__expire_at

    @expire_at.setter
    def expire_at(self, value):
        self.__expire_at = value


    def to_ams_json(self): 
        json_str = json.dumps(obj=self.to_ams_dict(), default=lambda o: o.to_ams_dict(), indent=3) 
        return json_str


    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "registration_update_period_request_id") and self.registration_update_period_request_id is not None:
            params['registrationUpdatePeriodRequestId'] = self.registration_update_period_request_id
        if hasattr(self, "tax_registration_id") and self.tax_registration_id is not None:
            params['taxRegistrationId'] = self.tax_registration_id
        if hasattr(self, "active_from") and self.active_from is not None:
            params['activeFrom'] = self.active_from
        if hasattr(self, "expire_at") and self.expire_at is not None:
            params['expireAt'] = self.expire_at
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'registrationUpdatePeriodRequestId' in response_body:
            self.__registration_update_period_request_id = response_body['registrationUpdatePeriodRequestId']
        if 'taxRegistrationId' in response_body:
            self.__tax_registration_id = response_body['taxRegistrationId']
        if 'activeFrom' in response_body:
            self.__active_from = response_body['activeFrom']
        if 'expireAt' in response_body:
            self.__expire_at = response_body['expireAt']
