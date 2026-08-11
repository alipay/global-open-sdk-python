import json
from com.alipay.ams.api.model.result import Result



from com.alipay.ams.api.response.alipay_response import AlipayResponse

class AlipayInvoiceCreateResponse(AlipayResponse):
    def __init__(self, rsp_body):
        super(AlipayResponse, self).__init__() 

        self.__result = None  # type: Result
        self.__invoice_id = None  # type: str
        self.__invoice_request_id = None  # type: str
        self.__status = None  # type: str
        self.__hosted_invoice_url = None  # type: str
        self.__send_status = None  # type: str
        self.parse_rsp_body(rsp_body) 


    @property
    def result(self):
        """Gets the result of this AlipayInvoiceCreateResponse.
        
        """
        return self.__result

    @result.setter
    def result(self, value):
        self.__result = value
    @property
    def invoice_id(self):
        """
        System-generated unique invoice ID. Used as the primary identifier for subsequent API calls (query, update, void). Cannot be null. Returned only when result.resultCode is SUCCESS.
        """
        return self.__invoice_id

    @invoice_id.setter
    def invoice_id(self, value):
        self.__invoice_id = value
    @property
    def invoice_request_id(self):
        """
        Echo-back of the merchant-supplied idempotency key from the request. Enables merchant-side correlation between request and response. Cannot be null. Returned only when result.resultCode is SUCCESS.
        """
        return self.__invoice_request_id

    @invoice_request_id.setter
    def invoice_request_id(self, value):
        self.__invoice_request_id = value
    @property
    def status(self):
        """
        Current invoice status: &#x60;DRAFT&#x60; or &#x60;OPEN&#x60;. Determines which subsequent operations are available (edit for DRAFT, pay for OPEN). Cannot be null. Returned only when result.resultCode is SUCCESS.
        """
        return self.__status

    @status.setter
    def status(self, value):
        self.__status = value
    @property
    def hosted_invoice_url(self):
        """
        URL to the customer-facing hosted invoice page. Auto-generated for OPEN invoices. When &#x60;status&#x3D;DRAFT&#x60;, this field is not returned - use the [Create View Link API](createViewLink.md) to generate a view URL for DRAFT invoices. Cannot be null when present. Returned only when result.resultCode is SUCCESS.
        """
        return self.__hosted_invoice_url

    @hosted_invoice_url.setter
    def hosted_invoice_url(self, value):
        self.__hosted_invoice_url = value
    @property
    def send_status(self):
        """
        Email send status. Returned only when &#x60;autoSend&#x3D;true&#x60; in the request. Enum values: &#x60;SENT&#x60; - email dispatched successfully; &#x60;FAILED&#x60; - email dispatch failed (retry allowed). Can be null (when &#x60;autoSend&#x3D;false&#x60; or absent). Returned only when result.resultCode is SUCCESS.
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
        if hasattr(self, "invoice_request_id") and self.invoice_request_id is not None:
            params['invoiceRequestId'] = self.invoice_request_id
        if hasattr(self, "status") and self.status is not None:
            params['status'] = self.status
        if hasattr(self, "hosted_invoice_url") and self.hosted_invoice_url is not None:
            params['hostedInvoiceUrl'] = self.hosted_invoice_url
        if hasattr(self, "send_status") and self.send_status is not None:
            params['sendStatus'] = self.send_status
        return params


    def parse_rsp_body(self, response_body):
        response_body = super(AlipayInvoiceCreateResponse, self).parse_rsp_body(response_body)
        if 'result' in response_body:
            self.__result = Result()
            self.__result.parse_rsp_body(response_body['result'])
        if 'invoiceId' in response_body:
            self.__invoice_id = response_body['invoiceId']
        if 'invoiceRequestId' in response_body:
            self.__invoice_request_id = response_body['invoiceRequestId']
        if 'status' in response_body:
            self.__status = response_body['status']
        if 'hostedInvoiceUrl' in response_body:
            self.__hosted_invoice_url = response_body['hostedInvoiceUrl']
        if 'sendStatus' in response_body:
            self.__send_status = response_body['sendStatus']
