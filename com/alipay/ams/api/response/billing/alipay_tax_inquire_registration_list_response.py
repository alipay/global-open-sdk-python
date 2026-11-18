import json
from com.alipay.ams.api.model.result import Result
from com.alipay.ams.api.model.paginator import Paginator



from com.alipay.ams.api.response.alipay_response import AlipayResponse

class AlipayTaxInquireRegistrationListResponse(AlipayResponse):
    def __init__(self, rsp_body):
        super(AlipayResponse, self).__init__() 

        self.__result = None  # type: Result
        self.__registrations = None  # type: [TaxRegistration]
        self.__paginator = None  # type: Paginator
        self.parse_rsp_body(rsp_body) 


    @property
    def result(self):
        """Gets the result of this AlipayTaxInquireRegistrationListResponse.
        
        """
        return self.__result

    @result.setter
    def result(self, value):
        self.__result = value
    @property
    def registrations(self):
        """
        The registrations. Note: See documentation for details.
        """
        return self.__registrations

    @registrations.setter
    def registrations(self, value):
        self.__registrations = value
    @property
    def paginator(self):
        """Gets the paginator of this AlipayTaxInquireRegistrationListResponse.
        
        """
        return self.__paginator

    @paginator.setter
    def paginator(self, value):
        self.__paginator = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "result") and self.result is not None:
            params['result'] = self.result
        if hasattr(self, "registrations") and self.registrations is not None:
            params['registrations'] = self.registrations
        if hasattr(self, "paginator") and self.paginator is not None:
            params['paginator'] = self.paginator
        return params


    def parse_rsp_body(self, response_body):
        response_body = super(AlipayTaxInquireRegistrationListResponse, self).parse_rsp_body(response_body)
        if 'result' in response_body:
            self.__result = Result()
            self.__result.parse_rsp_body(response_body['result'])
        if 'registrations' in response_body:
            self.__registrations = []
            for item in response_body['registrations']:
                obj = TaxRegistration()
                obj.parse_rsp_body(item)
                self.__registrations.append(obj)
        if 'paginator' in response_body:
            self.__paginator = Paginator()
            self.__paginator.parse_rsp_body(response_body['paginator'])
