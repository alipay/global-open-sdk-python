import json
from com.alipay.ams.api.model.result import Result



from com.alipay.ams.api.response.alipay_response import AlipayResponse

class AlipayCreditNoteVoidResponse(AlipayResponse):
    def __init__(self, rsp_body):
        super(AlipayResponse, self).__init__() 

        self.__result = None  # type: Result
        self.__credit_note_id = None  # type: str
        self.__status = None  # type: str
        self.__voided_at = None  # type: str
        self.parse_rsp_body(rsp_body) 


    @property
    def result(self):
        """Gets the result of this AlipayCreditNoteVoidResponse.
        
        """
        return self.__result

    @result.setter
    def result(self, value):
        self.__result = value
    @property
    def credit_note_id(self):
        """
        The credit note ID. Maximum length: 64 characters. Note: See documentation for details.
        """
        return self.__credit_note_id

    @credit_note_id.setter
    def credit_note_id(self, value):
        self.__credit_note_id = value
    @property
    def status(self):
        """
        The current status. Maximum length: 32 characters. Note: See documentation for details.
        """
        return self.__status

    @status.setter
    def status(self, value):
        self.__status = value
    @property
    def voided_at(self):
        """
        The voided at. Maximum length: 29 characters. Note: See documentation for details.
        """
        return self.__voided_at

    @voided_at.setter
    def voided_at(self, value):
        self.__voided_at = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "result") and self.result is not None:
            params['result'] = self.result
        if hasattr(self, "credit_note_id") and self.credit_note_id is not None:
            params['creditNoteId'] = self.credit_note_id
        if hasattr(self, "status") and self.status is not None:
            params['status'] = self.status
        if hasattr(self, "voided_at") and self.voided_at is not None:
            params['voidedAt'] = self.voided_at
        return params


    def parse_rsp_body(self, response_body):
        response_body = super(AlipayCreditNoteVoidResponse, self).parse_rsp_body(response_body)
        if 'result' in response_body:
            self.__result = Result()
            self.__result.parse_rsp_body(response_body['result'])
        if 'creditNoteId' in response_body:
            self.__credit_note_id = response_body['creditNoteId']
        if 'status' in response_body:
            self.__status = response_body['status']
        if 'voidedAt' in response_body:
            self.__voided_at = response_body['voidedAt']
