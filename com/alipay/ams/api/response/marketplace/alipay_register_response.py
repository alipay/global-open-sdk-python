import json
from com.alipay.ams.api.model.result import Result



from com.alipay.ams.api.response.alipay_response import AlipayResponse

class AlipayRegisterResponse(AlipayResponse):
    def __init__(self, rsp_body):
        super(AlipayResponse, self).__init__() 

        self.__result = None  # type: Result
        self.__registration_status = None  # type: str
        self.parse_rsp_body(rsp_body) 


    @property
    def result(self):
        """Gets the result of this AlipayRegisterResponse.
        
        """
        return self.__result

    @result.setter
    def result(self, value):
        self.__result = value
    @property
    def registration_status(self):
        """
        The registration status of the merchant. The value of this parameter is fixed to PROCESSING.   Get the sub-merchant&#39;s registration result from the notifyRegistration interface.   This parameter is returned when the value of result.resultStatus is S.    More information:  Maximum length: 64 characters
        """
        return self.__registration_status

    @registration_status.setter
    def registration_status(self, value):
        self.__registration_status = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "result") and self.result is not None:
            params['result'] = self.result
        if hasattr(self, "registration_status") and self.registration_status is not None:
            params['registrationStatus'] = self.registration_status
        return params


    def parse_rsp_body(self, response_body):
        response_body = super(AlipayRegisterResponse, self).parse_rsp_body(response_body)
        if 'result' in response_body:
            self.__result = Result()
            self.__result.parse_rsp_body(response_body['result'])
        if 'registrationStatus' in response_body:
            self.__registration_status = response_body['registrationStatus']
