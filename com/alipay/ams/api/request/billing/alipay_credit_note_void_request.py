import json



from com.alipay.ams.api.request.alipay_request import AlipayRequest

class AlipayCreditNoteVoidRequest(AlipayRequest):
    def __init__(self):
        super(AlipayCreditNoteVoidRequest, self).__init__("/ams/api/v1/billing/creditNote/void") 

        self.__credit_note_id = None  # type: str
        self.__reason = None  # type: str
        

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
    def reason(self):
        """
        The reason for the status change. Maximum length: 512 characters.
        """
        return self.__reason

    @reason.setter
    def reason(self, value):
        self.__reason = value


    def to_ams_json(self): 
        json_str = json.dumps(obj=self.to_ams_dict(), default=lambda o: o.to_ams_dict(), indent=3) 
        return json_str


    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "credit_note_id") and self.credit_note_id is not None:
            params['creditNoteId'] = self.credit_note_id
        if hasattr(self, "reason") and self.reason is not None:
            params['reason'] = self.reason
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'creditNoteId' in response_body:
            self.__credit_note_id = response_body['creditNoteId']
        if 'reason' in response_body:
            self.__reason = response_body['reason']
