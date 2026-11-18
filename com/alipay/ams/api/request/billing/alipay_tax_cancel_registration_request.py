import json



from com.alipay.ams.api.request.alipay_request import AlipayRequest

class AlipayTaxCancelRegistrationRequest(AlipayRequest):
    def __init__(self):
        super(AlipayTaxCancelRegistrationRequest, self).__init__("/ams/api/v1/tax/cancelRegistration") 

        self.__registration_cancel_request_id = None  # type: str
        self.__tax_registration_id = None  # type: str
        

    @property
    def registration_cancel_request_id(self):
        """
        The unique ID assigned by a merchant to identify a tax registration cancellation request. Any repeated request using an accepted ID returns REPEATED_SUBMIT. Maximum length: 64 characters.
        """
        return self.__registration_cancel_request_id

    @registration_cancel_request_id.setter
    def registration_cancel_request_id(self, value):
        self.__registration_cancel_request_id = value
    @property
    def tax_registration_id(self):
        """
        The unique ID assigned by Antom to identify a tax registration. Maximum length: 64 characters.
        """
        return self.__tax_registration_id

    @tax_registration_id.setter
    def tax_registration_id(self, value):
        self.__tax_registration_id = value


    def to_ams_json(self): 
        json_str = json.dumps(obj=self.to_ams_dict(), default=lambda o: o.to_ams_dict(), indent=3) 
        return json_str


    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "registration_cancel_request_id") and self.registration_cancel_request_id is not None:
            params['registrationCancelRequestId'] = self.registration_cancel_request_id
        if hasattr(self, "tax_registration_id") and self.tax_registration_id is not None:
            params['taxRegistrationId'] = self.tax_registration_id
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'registrationCancelRequestId' in response_body:
            self.__registration_cancel_request_id = response_body['registrationCancelRequestId']
        if 'taxRegistrationId' in response_body:
            self.__tax_registration_id = response_body['taxRegistrationId']
