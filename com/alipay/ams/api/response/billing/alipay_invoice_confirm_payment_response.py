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
        Invoice ID for which payment was confirmed (echo-back of request). Cannot be null. Returned only when result.resultCode is SUCCESS.
        """
        return self.__invoice_id

    @invoice_id.setter
    def invoice_id(self, value):
        self.__invoice_id = value
    @property
    def status(self):
        """
        New invoice status after confirmation: &#x60;PAID&#x60;. The invoice is now in a terminal paid state. Cannot be null. Returned only when result.resultCode is SUCCESS.
        """
        return self.__status

    @status.setter
    def status(self, value):
        self.__status = value
    @property
    def receipt_id(self):
        """
        Auto-generated receipt ID for the payment. Format: &#x60;rcpt_&#x60; + 10-char alphanumeric. The receipt confirms the payment and can be used with the Receipt Details and Send Receipt APIs. Cannot be null. Returned only when result.resultCode is SUCCESS.
        """
        return self.__receipt_id

    @receipt_id.setter
    def receipt_id(self, value):
        self.__receipt_id = value
    @property
    def invoice_note(self):
        """
        Echo-back of the &#x60;invoiceNote&#x60; provided in the request, if any. The note is stored in the &#x60;invoiceNotes&#x60; array in the invoice metadata with &#x60;action&#x3D;paid&#x60;. Can be null (no note provided). Returned only when result.resultCode is SUCCESS.
        """
        return self.__invoice_note

    @invoice_note.setter
    def invoice_note(self, value):
        self.__invoice_note = value
    @property
    def paid_at(self):
        """
        Timestamp when the payment was confirmed (ISO 8601, e.g., &#x60;2026-05-10T14:30:00+00:00&#x60;). Sourced from the delegate result&#39;s &#x60;paidTime&#x60;, which is set during the 3-way atomic write. This ensures consistency with the actual payment confirmation time in the database. Cannot be null. Returned only when result.resultCode is SUCCESS.
        """
        return self.__paid_at

    @paid_at.setter
    def paid_at(self, value):
        self.__paid_at = value
    @property
    def send_status(self):
        """
        Email send status for receipt email. Returned only when &#x60;autoSend&#x3D;true&#x60; in the request. Enum values: &#x60;SENT&#x60; - email dispatched successfully; &#x60;FAILED&#x60; - email dispatch failed (retry allowed). Can be null (when &#x60;autoSend&#x3D;false&#x60; or absent). Returned only when result.resultCode is SUCCESS.
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
