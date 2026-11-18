import json
from com.alipay.ams.api.model.result import Result



from com.alipay.ams.api.response.alipay_response import AlipayResponse

class AlipaySupplyDefenseDocumentResponse(AlipayResponse):
    def __init__(self, rsp_body):
        super(AlipayResponse, self).__init__() 

        self.__result = None  # type: Result
        self.__dispute_id = None  # type: str
        self.__dispute_resolution_time = None  # type: str
        self.parse_rsp_body(rsp_body) 


    @property
    def result(self):
        """Gets the result of this AlipaySupplyDefenseDocumentResponse.
        
        """
        return self.__result

    @result.setter
    def result(self, value):
        self.__result = value
    @property
    def dispute_id(self):
        """
        The unique ID assigned by Antom to identify a dispute.  Note: This prameter is returned when the value of resultCode is SUCCESS.  More information:  Maximum length: 64 characters
        """
        return self.__dispute_id

    @dispute_id.setter
    def dispute_id(self, value):
        self.__dispute_id = value
    @property
    def dispute_resolution_time(self):
        """
        The time when you upload the dispute defense document.  Note: This prameter is returned when the value of resultCode is SUCCESS.  More information:  Maximum length: 64 characters
        """
        return self.__dispute_resolution_time

    @dispute_resolution_time.setter
    def dispute_resolution_time(self, value):
        self.__dispute_resolution_time = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "result") and self.result is not None:
            params['result'] = self.result
        if hasattr(self, "dispute_id") and self.dispute_id is not None:
            params['disputeId'] = self.dispute_id
        if hasattr(self, "dispute_resolution_time") and self.dispute_resolution_time is not None:
            params['disputeResolutionTime'] = self.dispute_resolution_time
        return params


    def parse_rsp_body(self, response_body):
        response_body = super(AlipaySupplyDefenseDocumentResponse, self).parse_rsp_body(response_body)
        if 'result' in response_body:
            self.__result = Result()
            self.__result.parse_rsp_body(response_body['result'])
        if 'disputeId' in response_body:
            self.__dispute_id = response_body['disputeId']
        if 'disputeResolutionTime' in response_body:
            self.__dispute_resolution_time = response_body['disputeResolutionTime']
