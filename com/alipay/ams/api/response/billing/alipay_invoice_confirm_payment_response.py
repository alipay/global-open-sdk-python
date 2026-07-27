import json
from com.alipay.ams.api.model.result import Result



from com.alipay.ams.api.response.alipay_response import AlipayResponse

class AlipayInvoiceConfirmPaymentResponse(AlipayResponse):
    def __init__(self, rsp_body):
        super(AlipayResponse, self).__init__() 

        self.__result = None  # type: Result
        self.__invoice_id = None  # type: str
        self.__status = None  # type: str
        self.__receipt_id = None  # type: str
        self.__invoice_note = None  # type: str
        self.__paid_at = None  # type: str
        self.__send_status = None  # type: str
        self.parse_rsp_body(rsp_body) 


    @property
    def result(self):
        """Gets the result of this AlipayInvoiceConfirmPaymentResponse.
        
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
    def receipt_id(self):
        """
        The receipt ID. Maximum length: 64 characters.
        """
        return self.__receipt_id

    @receipt_id.setter
    def receipt_id(self, value):
        self.__receipt_id = value
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
    def paid_at(self):
        """
        The paid at. Maximum length: 24 characters.
        """
        return self.__paid_at

    @paid_at.setter
    def paid_at(self, value):
        self.__paid_at = value
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
        if hasattr(self, "receipt_id") and self.receipt_id is not None:
            params['receiptId'] = self.receipt_id
        if hasattr(self, "invoice_note") and self.invoice_note is not None:
            params['invoiceNote'] = self.invoice_note
        if hasattr(self, "paid_at") and self.paid_at is not None:
            params['paidAt'] = self.paid_at
        if hasattr(self, "send_status") and self.send_status is not None:
            params['sendStatus'] = self.send_status
        return params


    def parse_rsp_body(self, response_body):
        response_body = super(AlipayInvoiceConfirmPaymentResponse, self).parse_rsp_body(response_body)
        if 'result' in response_body:
            self.__result = Result()
            self.__result.parse_rsp_body(response_body['result'])
        if 'invoiceId' in response_body:
            self.__invoice_id = response_body['invoiceId']
        if 'status' in response_body:
            self.__status = response_body['status']
        if 'receiptId' in response_body:
            self.__receipt_id = response_body['receiptId']
        if 'invoiceNote' in response_body:
            self.__invoice_note = response_body['invoiceNote']
        if 'paidAt' in response_body:
            self.__paid_at = response_body['paidAt']
        if 'sendStatus' in response_body:
            self.__send_status = response_body['sendStatus']
