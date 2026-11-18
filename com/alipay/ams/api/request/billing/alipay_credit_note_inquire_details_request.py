import json



from com.alipay.ams.api.request.alipay_request import AlipayRequest

class AlipayCreditNoteInquireDetailsRequest(AlipayRequest):
    def __init__(self):
        super(AlipayCreditNoteInquireDetailsRequest, self).__init__("/ams/api/v1/billing/creditNote/inquireDetails") 

        self.__credit_note_id = None  # type: str
        

    @property
    def credit_note_id(self):
        """
        The credit note ID. Maximum length: 64 characters.
        """
        return self.__credit_note_id

    @credit_note_id.setter
    def credit_note_id(self, value):
        self.__credit_note_id = value


    def to_ams_json(self): 
        json_str = json.dumps(obj=self.to_ams_dict(), default=lambda o: o.to_ams_dict(), indent=3) 
        return json_str


    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "credit_note_id") and self.credit_note_id is not None:
            params['creditNoteId'] = self.credit_note_id
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'creditNoteId' in response_body:
            self.__credit_note_id = response_body['creditNoteId']
