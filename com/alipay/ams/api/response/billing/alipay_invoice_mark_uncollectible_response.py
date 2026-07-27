import json
from com.alipay.ams.api.model.result import Result



from com.alipay.ams.api.response.alipay_response import AlipayResponse

class AlipayInvoiceMarkUncollectibleResponse(AlipayResponse):
    def __init__(self, rsp_body):
        super(AlipayResponse, self).__init__() 

        self.__result = None  # type: Result
        self.__invoice_id = None  # type: str
        self.__status = None  # type: str
        self.__marked_uncollectible_at = None  # type: str
        self.__invoice_note = None  # type: str
        self.parse_rsp_body(rsp_body) 


    @property
    def result(self):
        """Gets the result of this AlipayInvoiceMarkUncollectibleResponse.
        
        """
        return self.__result

    @result.setter
    def result(self, value):
        self.__result = value
    @property
    def invoice_id(self):
        """
        The invoice ID. Maximum length: 64 characters.
        """
        return self.__invoice_id

    @invoice_id.setter
    def invoice_id(self, value):
        self.__invoice_id = value
    @property
    def status(self):
        """
        The current status. Maximum length: 16 characters.
        """
        return self.__status

    @status.setter
    def status(self, value):
        self.__status = value
    @property
    def marked_uncollectible_at(self):
        """
        The marked uncollectible at. Maximum length: 24 characters.
        """
        return self.__marked_uncollectible_at

    @marked_uncollectible_at.setter
    def marked_uncollectible_at(self, value):
        self.__marked_uncollectible_at = value
    @property
    def invoice_note(self):
        """
        The invoice note. Maximum length: 512 characters.
        """
        return self.__invoice_note

    @invoice_note.setter
    def invoice_note(self, value):
        self.__invoice_note = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "result") and self.result is not None:
            params['result'] = self.result
        if hasattr(self, "invoice_id") and self.invoice_id is not None:
            params['invoiceId'] = self.invoice_id
        if hasattr(self, "status") and self.status is not None:
            params['status'] = self.status
        if hasattr(self, "marked_uncollectible_at") and self.marked_uncollectible_at is not None:
            params['markedUncollectibleAt'] = self.marked_uncollectible_at
        if hasattr(self, "invoice_note") and self.invoice_note is not None:
            params['invoiceNote'] = self.invoice_note
        return params


    def parse_rsp_body(self, response_body):
        response_body = super(AlipayInvoiceMarkUncollectibleResponse, self).parse_rsp_body(response_body)
        if 'result' in response_body:
            self.__result = Result()
            self.__result.parse_rsp_body(response_body['result'])
        if 'invoiceId' in response_body:
            self.__invoice_id = response_body['invoiceId']
        if 'status' in response_body:
            self.__status = response_body['status']
        if 'markedUncollectibleAt' in response_body:
            self.__marked_uncollectible_at = response_body['markedUncollectibleAt']
        if 'invoiceNote' in response_body:
            self.__invoice_note = response_body['invoiceNote']
