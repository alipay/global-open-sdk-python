import json
from com.alipay.ams.api.model.result import Result



from com.alipay.ams.api.response.alipay_response import AlipayResponse

class AlipayInvoiceUpdateResponse(AlipayResponse):
    def __init__(self, rsp_body):
        super(AlipayResponse, self).__init__() 

        self.__result = None  # type: Result
        self.__invoice_id = None  # type: str
        self.__status = None  # type: str
        self.__previous_invoice_id = None  # type: str
        self.parse_rsp_body(rsp_body) 


    @property
    def result(self):
        """Gets the result of this AlipayInvoiceUpdateResponse.
        
        """
        return self.__result

    @result.setter
    def result(self, value):
        self.__result = value
    @property
    def invoice_id(self):
        """
        Invoice ID (echo-back). Cannot be null. Returned only when result.resultCode is SUCCESS.
        """
        return self.__invoice_id

    @invoice_id.setter
    def invoice_id(self, value):
        self.__invoice_id = value
    @property
    def status(self):
        """
        Invoice status after edit: always &#x60;DRAFT&#x60;. The edit API only operates on DRAFT invoices - successful edits always return &#x60;DRAFT&#x60; status. This confirms the invoice remains in editable state. See enum table below. Cannot be null. Returned only when result.resultCode is SUCCESS.
        """
        return self.__status

    @status.setter
    def status(self, value):
        self.__status = value
    @property
    def previous_invoice_id(self):
        """
        Previous invoice ID when customer reassignment occurred (soft-delete + recreate). Null for normal updates. Populated only when &#x60;customerId&#x60; was changed, causing the invoice to be recreated with a new ID in a different shard. Returned only when result.resultCode is SUCCESS.
        """
        return self.__previous_invoice_id

    @previous_invoice_id.setter
    def previous_invoice_id(self, value):
        self.__previous_invoice_id = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "result") and self.result is not None:
            params['result'] = self.result
        if hasattr(self, "invoice_id") and self.invoice_id is not None:
            params['invoiceId'] = self.invoice_id
        if hasattr(self, "status") and self.status is not None:
            params['status'] = self.status
        if hasattr(self, "previous_invoice_id") and self.previous_invoice_id is not None:
            params['previousInvoiceId'] = self.previous_invoice_id
        return params


    def parse_rsp_body(self, response_body):
        response_body = super(AlipayInvoiceUpdateResponse, self).parse_rsp_body(response_body)
        if 'result' in response_body:
            self.__result = Result()
            self.__result.parse_rsp_body(response_body['result'])
        if 'invoiceId' in response_body:
            self.__invoice_id = response_body['invoiceId']
        if 'status' in response_body:
            self.__status = response_body['status']
        if 'previousInvoiceId' in response_body:
            self.__previous_invoice_id = response_body['previousInvoiceId']
