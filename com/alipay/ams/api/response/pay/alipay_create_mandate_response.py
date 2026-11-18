import json
from com.alipay.ams.api.model.result import Result



from com.alipay.ams.api.response.alipay_response import AlipayResponse

class AlipayCreateMandateResponse(AlipayResponse):
    def __init__(self, rsp_body):
        super(AlipayResponse, self).__init__() 

        self.__result = None  # type: Result
        self.__mandate_request_id = None  # type: str
        self.__mandate_id = None  # type: str
        self.__valid_from = None  # type: str
        self.__valid_until = None  # type: str
        self.parse_rsp_body(rsp_body) 


    @property
    def result(self):
        """Gets the result of this AlipayCreateMandateResponse.
        
        """
        return self.__result

    @result.setter
    def result(self, value):
        self.__result = value
    @property
    def mandate_request_id(self):
        """
        Echoed only when the request ID was parsed successfully. Correlates the request and does not establish success.
        """
        return self.__mandate_request_id

    @mandate_request_id.setter
    def mandate_request_id(self, value):
        self.__mandate_request_id = value
    @property
    def mandate_id(self):
        """
        The Antom one-time mandate ID. Returned only when result.resultStatus is S; use for one subsequent payment intent. A successful replay returns the same ID, not a new mandate.
        """
        return self.__mandate_id

    @mandate_id.setter
    def mandate_id(self, value):
        self.__mandate_id = value
    @property
    def valid_from(self):
        """
        The mandate validity start, returned only when result.resultStatus is S. ISO 8601 offset date-time string, for example 2026-07-23T10:00:00+08:00. Channel time is converted using Asia/Shanghai by the service; SDKs preserve the string without timezone conversion.
        """
        return self.__valid_from

    @valid_from.setter
    def valid_from(self, value):
        self.__valid_from = value
    @property
    def valid_until(self):
        """
        The mandate expiration, returned only when result.resultStatus is S. ISO 8601 offset date-time string, for example 2026-08-22T10:00:00+08:00; it must be later than validFrom. Channel time is converted using Asia/Shanghai by the service. Successful replay preserves the original validity window.
        """
        return self.__valid_until

    @valid_until.setter
    def valid_until(self, value):
        self.__valid_until = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "result") and self.result is not None:
            params['result'] = self.result
        if hasattr(self, "mandate_request_id") and self.mandate_request_id is not None:
            params['mandateRequestId'] = self.mandate_request_id
        if hasattr(self, "mandate_id") and self.mandate_id is not None:
            params['mandateId'] = self.mandate_id
        if hasattr(self, "valid_from") and self.valid_from is not None:
            params['validFrom'] = self.valid_from
        if hasattr(self, "valid_until") and self.valid_until is not None:
            params['validUntil'] = self.valid_until
        return params


    def parse_rsp_body(self, response_body):
        response_body = super(AlipayCreateMandateResponse, self).parse_rsp_body(response_body)
        if 'result' in response_body:
            self.__result = Result()
            self.__result.parse_rsp_body(response_body['result'])
        if 'mandateRequestId' in response_body:
            self.__mandate_request_id = response_body['mandateRequestId']
        if 'mandateId' in response_body:
            self.__mandate_id = response_body['mandateId']
        if 'validFrom' in response_body:
            self.__valid_from = response_body['validFrom']
        if 'validUntil' in response_body:
            self.__valid_until = response_body['validUntil']
