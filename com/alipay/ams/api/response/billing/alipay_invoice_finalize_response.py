import json
from com.alipay.ams.api.model.result import Result



from com.alipay.ams.api.response.alipay_response import AlipayResponse

class AlipayInvoiceFinalizeResponse(AlipayResponse):
    def __init__(self, rsp_body):
        super(AlipayResponse, self).__init__() 

        self.__result = None  # type: Result
        self.__invoice_id = None  # type: str
        self.__status = None  # type: str
        self.__hosted_invoice_url = None  # type: str
        self.__finalized_at = None  # type: str
        self.__invoice_note = None  # type: str
        self.__send_status = None  # type: str
        self.parse_rsp_body(rsp_body) 


    @property
    def result(self):
        """Gets the result of this AlipayInvoiceFinalizeResponse.
        
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
    def hosted_invoice_url(self):
        """
        The hosted invoice url. Maximum length: 2048 characters.
        """
        return self.__hosted_invoice_url

    @hosted_invoice_url.setter
    def hosted_invoice_url(self, value):
        self.__hosted_invoice_url = value
    @property
    def finalized_at(self):
        """
        The finalized at. Maximum length: 24 characters.
        """
        return self.__finalized_at

    @finalized_at.setter
    def finalized_at(self, value):
        self.__finalized_at = value
    @property
    def invoice_note(self):
        """
        The invoice note. Maximum length: 512 characters.
        """
        return self.__invoice_note

    @invoice_note.setter
    def invoice_note(self, value):
        self.__invoice_note = value
    @property
    def send_status(self):
        """
        The email sending status. Maximum length: 16 characters. Note: See documentation for details.
        """
        return self.__send_status

    @send_status.setter
    def send_status(self, value):
        self.__send_status = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "result") and self.result is not None:
            params['result'] = self.result
        if hasattr(self, "invoice_id") and self.invoice_id is not None:
            params['invoiceId'] = self.invoice_id
        if hasattr(self, "status") and self.status is not None:
            params['status'] = self.status
        if hasattr(self, "hosted_invoice_url") and self.hosted_invoice_url is not None:
            params['hostedInvoiceUrl'] = self.hosted_invoice_url
        if hasattr(self, "finalized_at") and self.finalized_at is not None:
            params['finalizedAt'] = self.finalized_at
        if hasattr(self, "invoice_note") and self.invoice_note is not None:
            params['invoiceNote'] = self.invoice_note
        if hasattr(self, "send_status") and self.send_status is not None:
            params['sendStatus'] = self.send_status
        return params


    def parse_rsp_body(self, response_body):
        response_body = super(AlipayInvoiceFinalizeResponse, self).parse_rsp_body(response_body)
        if 'result' in response_body:
            self.__result = Result()
            self.__result.parse_rsp_body(response_body['result'])
        if 'invoiceId' in response_body:
            self.__invoice_id = response_body['invoiceId']
        if 'status' in response_body:
            self.__status = response_body['status']
        if 'hostedInvoiceUrl' in response_body:
            self.__hosted_invoice_url = response_body['hostedInvoiceUrl']
        if 'finalizedAt' in response_body:
            self.__finalized_at = response_body['finalizedAt']
        if 'invoiceNote' in response_body:
            self.__invoice_note = response_body['invoiceNote']
        if 'sendStatus' in response_body:
            self.__send_status = response_body['sendStatus']
